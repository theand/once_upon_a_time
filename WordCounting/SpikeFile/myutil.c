#include "myutil.h"

char *_progName;

// malloc �� �����ڵ鸵�� �߰���Ų ������ wrapper function
void *emalloc(size_t n)
{
	void *p;
	p = (void *) malloc(n);
	if (p == NULL)  
		eprintf("malloc of %u bytes failed:", n);
	return p;
}

//error printf
void eprintf(char *fmt, ...)
{
	va_list args;

	fflush(stdout);
	if( getProgName() != NULL)
		fprintf(stderr, "%s: ", getProgName());
	free(getProgName());
	va_start(args,fmt);
	vfprintf(stderr, fmt, args);
	va_end(args);
	if( fmt[0] != '\0' && fmt[strlen(fmt)-1] ==':' )
		fprintf(stderr, "%s", strerror(errno));
	fprintf(stderr, "\n");
	exit(EXIT_FAILURE);
}

void setProgName(const char *aStr)
{
	assert(aStr!=NULL);
	_progName = estrdup(aStr);
}

char *getProgName(void)
{
	assert(_progName!=NULL);
	return _progName;
}

//strdup
char * estrdup(const char *aStr)
{
	char *t;

	t=(char *)malloc(strlen(aStr)+1);
	if(NULL==t)
		eprintf("estrdup(\"%.20s\") failed.", aStr);
	strcpy(t,aStr);
	return t;
}


// ������ ��� FILE * �� �����Ѵ�.
// ������ ���� ��쿡 ���� ����ó������� �߰��� ������ wrapper function
FILE *efopen(char *name, char *mode)
{
	FILE *tmp;

	assert(name != NULL && mode != NULL);

	if ((tmp = fopen(name, mode)) == NULL) 
		eprintf("efopen(name=\"%s\",mode=\"%s\") failed:", name, mode);
	return tmp;
}

// �̹� ������ ������ ���ڷ� �޾Ƽ� �ݴ´�.
void closeFile(FILE * t)
{
	assert(t != NULL);
	fclose(t);
}


/////////////// End of File ////////////////////
