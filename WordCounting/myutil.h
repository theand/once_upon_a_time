
#ifndef _MY_UTIL_
#define _MY_UTIL_

#include <assert.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>


#define StrLess(strLeft, strRight)\
    (strcmp(strLeft, strRight)<0) 
#define StrGreater(strLeft, strRight)\
	(strcmp(strLeft, strRight)>0) 
#define StrEqual(strLeft, strRight)\
	(strcmp(strLeft, strRight)==0) 
#define assertEquals( left, right )\
	( assert( (left) == (right) ) )
#define assertStrEquals( left, right )\
	( assertTrue( StrEqual( (left), (right) ) )  )
#define assertTrue( statement )\
	( assert( (statement) == true ) )
#define assertFalse( statement )\
	( assert( (statement) == false ) )

FILE *efopen(char *name, char *mode);
void closeFile(FILE *t);
void *emalloc(size_t n);
void eprintf(char *fmt, ...);
char *estrdup(const char *aStr);
void setProgName(const char *aStr);
char *getProgName(void);


#ifndef __cplusplus
enum {true=1, false=0};
#endif

extern char *progName;
#endif
//////////////////////// End Of File /////////////////////////////
