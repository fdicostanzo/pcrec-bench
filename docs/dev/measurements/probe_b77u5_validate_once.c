/* SCRATCH measurement only: find-all '.' under PCRE2_UTF, with (mode 1) and
   without (mode 0) NO_UTF_CHECK on calls after the first. Hand prototypes. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
typedef struct pcre2_real_code_8 pcre2_code_8;
typedef struct pcre2_real_match_data_8 pcre2_match_data_8;
pcre2_code_8 *pcre2_compile_8(const unsigned char*, size_t, uint32_t, int*, size_t*, void*);
pcre2_match_data_8 *pcre2_match_data_create_from_pattern_8(const pcre2_code_8*, void*);
int pcre2_match_8(const pcre2_code_8*, const unsigned char*, size_t, size_t, uint32_t, pcre2_match_data_8*, void*);
size_t *pcre2_get_ovector_pointer_8(pcre2_match_data_8*);
int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "rb"); fseek(f,0,SEEK_END); long n = ftell(f); rewind(f);
  unsigned char *b = malloc(n); if (fread(b,1,n,f) != (size_t)n) return 2; fclose(f);
  int ec; size_t eo; int mode = atoi(argv[2]);
  pcre2_code_8 *c = pcre2_compile_8((const unsigned char*)".", 1, 0x00080000u, &ec, &eo, NULL);
  pcre2_match_data_8 *md = pcre2_match_data_create_from_pattern_8(c, NULL);
  struct timespec t0,t1; clock_gettime(CLOCK_MONOTONIC,&t0);
  size_t pos=0; long cnt=0;
  while (pos <= (size_t)n) {
    uint32_t opt = (mode && cnt) ? 0x40000000u : 0;
    int rc = pcre2_match_8(c, b, n, pos, opt, md, NULL);
    if (rc < 0) break;
    size_t *ov = pcre2_get_ovector_pointer_8(md);
    cnt++;
    if (ov[1] > ov[0]) pos = ov[1]; else { pos = ov[0]+1; while (pos < (size_t)n && (b[pos]&0xC0)==0x80) pos++; }
  }
  clock_gettime(CLOCK_MONOTONIC,&t1);
  printf("mode=%d count=%ld secs=%.3f\n", mode, cnt, (t1.tv_sec-t0.tv_sec)+(t1.tv_nsec-t0.tv_nsec)/1e9);
  return 0;
}
