// U8 repro: RE2 (EncodingUTF8) reports an empty-width `\B` match BETWEEN
// THE BYTES of one multi-byte UTF-8 character, rather than only at
// character boundaries.
//
// Subject: "aé" -- UTF-8 bytes 61 C3 A9 (byte offsets 0,1,2; character
// offsets 0,1,2 in codepoints "a", U+00E9). \B ("not at a word
// boundary") is the complement of \b; RE2's own syntax documentation
// (doc/syntax.txt) defines BOTH purely in terms of ASCII word
// characters:
//     \b   at ASCII word boundary (\w on one side and \W, \A, or \z on the other)
//     \B   not at ASCII word boundary
// and separately states its Perl character classes (\w among them)
// are "all ASCII-only". Under EncodingUTF8, RE2's automaton is
// compiled over UTF-8 BYTES (each multi-byte character becomes several
// byte-range NFA transitions) and \b/\B are evaluated per BYTE, not per
// decoded character: a continuation byte (C3, A9, both >= 0x80) is
// never \w by the ASCII-only definition, so BOTH sides of the boundary
// INSIDE "é" (between byte 1 and byte 2) read "not a word character" --
// making \B match there, at a byte offset with no character boundary
// at all.
//
// This repro isolates that with re2/re2.h directly (RE2::Options with
// EncodingUTF8, RE2::Match with an advancing startpos -- the same
// "advance after an empty match" loop pcrec-bench's own
// testees/re2/driver.cc and testees/pcre2/driver.c implement) --
// nothing from pcrec-bench is linked or executed.
//
// Build: g++ -O2 -std=c++17 $(pkg-config --cflags re2) repro.cc
//        $(pkg-config --libs re2) -o repro   (see run.sh)

#include <re2/re2.h>

#include <cstdio>
#include <string>

int main() {
    RE2::Options opts;
    opts.set_encoding(RE2::Options::EncodingUTF8);
    RE2 re("\\B", opts);
    if (!re.ok()) {
        std::fprintf(stderr, "RE2 compile failed: %s\n", re.error().c_str());
        return 2;
    }

    // "a" (0x61) + U+00E9 "e-acute" encoded as UTF-8 (0xC3 0xA9).
    // Character boundaries (as a rune-aware reader sees them): 0, 1, 3.
    // Byte offset 2 sits INSIDE the two-byte encoding of U+00E9.
    const unsigned char raw[] = {0x61, 0xC3, 0xA9};
    absl::string_view text(reinterpret_cast<const char *>(raw), sizeof(raw));

    bool saw_midchar = false;
    size_t startpos = 0;
    while (startpos <= text.size()) {
        absl::string_view m;
        if (!re.Match(text, startpos, text.size(), RE2::UNANCHORED, &m, 1))
            break;
        size_t so = static_cast<size_t>(m.data() - text.data());
        size_t eo = so + m.size();
        bool midchar = (so == 2); // between the two bytes of U+00E9
        std::printf("\\B match at byte [%zu,%zu)%s\n", so, eo,
                     midchar ? "  <-- INSIDE the 2-byte encoding of U+00E9" : "");
        if (midchar) saw_midchar = true;
        // advance rule: an empty match makes no forward progress on its
        // own, so step past ITS OWN position by one byte; a non-empty
        // match advances to its own end (mirrors this project's own
        // find-all advance rule, KB-17).
        startpos = (eo == so) ? so + 1 : eo;
    }

    if (saw_midchar) {
        std::printf("PRESENT: RE2 reports \\B at a byte offset with no "
                    "character boundary (inside U+00E9's 2-byte encoding)\n");
        return 0;
    }
    std::printf("ABSENT: no \\B match landed inside a multi-byte character\n");
    return 1;
}
