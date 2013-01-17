
/*
 * wc.c 
 */

#include "wc.h"
#include <string.h>
#include <ctype.h>
//#define DEBUG 

//////////////////// Global Data ////////////////////////

int isPrintLine;
int isPrintChar;
int isPrintWord;

int _numOfWords;
int _numOfLines;
int _numOfChars;

char *_fileName;
FILE *_fp=NULL;


////////////// Function //////////////////


void handleArgument(int argc, char **argv)
{
	//TODO - multiple argument
	if( argc==2 ){
		setFileName(argv[1]);
	}
	else if( argc==1 ){
		setFileName("stdin");
	}
	else{
		fprintf(stderr, "ERROR: this version of program doesn't support multiple arguments.\n");
		exit(EXIT_FAILURE);
	}
}
/////////////////////////////////////////////////

int getNumOfLines(void)
{
	return _numOfLines;
}
int getNumOfChars(void)
{
	return _numOfChars;
}
int getNumOfWords(void)
{
	return _numOfWords;
}
void setPrintMode(int mode)
{
	enum {line=4, word=2, chars=1, on=1, off=0};

	if( (mode & line) == line )
		isPrintLine =on;
	if( (mode & word) == word)
		isPrintWord = on;
	if( (mode & chars) == chars )
		isPrintChar = on;
}

void printResult(void)
{
	if( isPrintWord )
		printf("Number of Words = %d\n", getNumOfWords() );
	if( isPrintChar )
		printf("Number of Chars = %d\n", getNumOfChars() );
	if( isPrintLine)
		printf("Number of Lines = %d\n", getNumOfLines() );
}
/////////////////////////////////////////////////

void setFileName(char *name)
{
	assert(name!=NULL);

	_fileName = estrdup(name);
}

char * getFileName(void)
{
	assert(_fileName != NULL);
	return _fileName;
}

void initLineList(void)
{
	char *name = getFileName();

	if( StrEqual(name, "stdin")  )
		_fp = stdin;
	else{
		if( _fp == NULL){
		_fp = efopen(name, "r");
		}
	}
}
/////////////////////////////////////////////////

char *getLine(void)
{
	static char line[81];
	
	fgets(line, 80, _fp);

	/*//Delete \n
	line[strlen(line)-1]='\0';*/

	if( hasNextLine() == false )
		return "";

	return line;
}

int hasNextLine(void)
{
	return !feof(_fp);
}
/////////////////////////////////////////////////

int countWord(const char *aLine)
{
	int numOfWord=0;
	char *word;
	char *line ;
	char *SEPARATOR = " \t\n,.:;<>[]&%%";

	line = estrdup(aLine);

	for( word = strtok(line, SEPARATOR ); word!=NULL ; word = strtok(NULL, SEPARATOR)){
	
#ifdef DEBUG
		printf("%s\n", word);
#endif
		numOfWord++;
		//TODO : countWord 에 insertWord 까지 있는 것이 좀 이상.
		insertWord(word);
	}
	_numOfWords+=numOfWord;
	return numOfWord;
}

int countLine(const char *aLine)
{

	int count=0;
	char *s;


	s=strchr(aLine, '\n');
	if( s == NULL )
		return 0;

	while( s != NULL ){
		count++;
		s = strchr(s+1, '\n');
	}
	_numOfLines += count;
	return count;
}
int countChar(const char *aLine)
{
	int i;
	int count=0;
	for(i=0; aLine[i] != '\0' ; i++)
		if( isalpha(aLine[i]) )
			count++; 
	_numOfChars+=count;
	return count; 
}


//////////////// End Of File //////////////////////
