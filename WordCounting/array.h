
/*
 * array.h
 * */

#ifndef _ARRAY_H_
#define _ARRAY_H_

typedef struct _WordList{
	char *word;
	int count;
}WordList;

//public
void insertWord(const char *aWord);
void printWordList(void);

//private
WordList *getNodeAt(const char *aWord);
int isInclude(const char *aWord);
int getIndexOf(const char *aWord); 
int getOccurrenceOf(const char *aWord);



#endif

/////////////////// End Of File ////////////////
