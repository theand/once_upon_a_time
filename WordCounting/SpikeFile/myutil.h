
#ifndef _MY_UTIL_
#define _MY_UTIL_

#include <assert.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

FILE *efopen(char *name, char *mode);
void closeFile(FILE *t);
void *emalloc(size_t n);
void eprintf(char *fmt, ...);
char *estrdup(const char *aStr);
void setProgName(const char *aStr);
char *getProgName(void);


extern char *progName;
#endif
//////////////////////// End Of File /////////////////////////////
