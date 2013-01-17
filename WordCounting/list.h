
#ifndef _LIST_H_
#define _LIST_H_


typedef struct WordList{
	char *word;
	int count;
	struct WordList *next;
}WordList;


//public
void insertWord(const char *aWord);
void printWordList(void);


//private
WordList *getNewNode(const char *aWord);
int isInclude(const char *aWord);
void increaseCountOf(WordList *aNode);
void insertNewNode(const char *aWord);


extern WordList *_startNode;
extern WordList *_lastNode;
#endif

///////// End Of File /////////////////
