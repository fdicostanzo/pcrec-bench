/* U15: print Oniguruma's default subexp-call max nest level. */
#include <stdio.h>
#include <oniguruma.h>
int main(void) { printf("%s %d\n", onig_version(), onig_get_subexp_call_max_nest_level()); return 0; }
