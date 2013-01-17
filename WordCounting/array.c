
/*
 * array.c
 * */


#include "myutil.h"
#include "array.h"

WordList _wordList[500];
int _currentInsertIndex=0;

void insertWord(const char *aWord)
{
	//TODO : free estrdup

	assert(aWord!=NULL);

	if( isInclude(aWord) ){
		_wordList[getIndexOf(aWord)].count++;
	}
	else{
		_wordList[_currentInsertIndex].word = estrdup(aWord);
		_wordList[_currentInsertIndex].count = 1;
		_currentInsertIndex++; 
	}
	//TODO free pointer.
	
}
int isInclude(const char *aWord)
{
	int i;

	for( i=0; i< _currentInsertIndex; i++)
		if( StrEqual(aWord, _wordList[i].word) )
			return true;

	return false; 
}

int getIndexOf(const char *aWord)
{
	int i;

	assert( isInclude(aWord) == true );

	for( i=0; i< _currentInsertIndex; i++)
		if( StrEqual(aWord, _wordList[i].word) )
			break;
	assertTrue( i != _currentInsertIndex );
	return i;
}

WordList *getNodeAt(const char *aWord)
{
	int i;
	for( i=0; i< _currentInsertIndex; i++)
		if( StrEqual(aWord, _wordList[i].word) )
			break; 
	return (&_wordList[i]);
}

/*
int getOccurrenceOf(const char *aWord)
{
	int i;
	assertTrue( aWord != NULL);
	i=getIndexOf(aWord);
	return _wordList[i].count;
}
*/
void printWordList(void)
{
	//TODO make flag
	int i;
	for(i=0;i< _currentInsertIndex; i++){
		printf("%s\t%d\n", _wordList[i].word, _wordList[i].count );
	}
}


/////////// End Of File /////////////////
