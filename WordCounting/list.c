
#include "list.h"
#include "myutil.h"

WordList *_startNode;
WordList *_lastNode;//TODO deprecated
WordList *_searchedNode;



void insertWord(const char *aWord)
{
	//TODO : free emalloc, estrdup

	if( _startNode == NULL )
		_lastNode =_startNode = getNewNode(aWord);
	else
		insertNewNode(aWord);

}
void insertNewNode(const char *aWord)
{
	WordList *newNode;
	WordList *prevNode;
	WordList *eachNode;

	newNode = (WordList *)getNewNode(aWord);

	prevNode = _startNode;
	for( eachNode = _startNode ; eachNode != NULL ; eachNode = eachNode->next ){
		if( StrLess(aWord, eachNode->word) ){
			if( eachNode == _startNode ){//맨처음
				newNode->next = eachNode;
				_startNode = newNode;//TODO 
			}
			else{//중간.
				newNode->next = eachNode;
				prevNode->next = newNode;
			}
			break;
		}
		else if( StrGreater(aWord, eachNode->word) ){//맨뒤
			if( eachNode->next == NULL ){
				eachNode->next = newNode;
				_lastNode = newNode;
				break;
			}
		}
		else if( StrEqual(aWord, eachNode->word) ){//같은글자 찾았을때.
			increaseCountOf(eachNode);
			free(newNode->word);
			free(newNode);
			break;
		}

		prevNode = eachNode;
	}
}
		

int isInclude(const char *aWord)
{
	WordList *tmpNode;
	for( tmpNode = _startNode; tmpNode != NULL ; tmpNode = tmpNode->next){
		if( StrEqual( tmpNode->word, aWord) ){
			_searchedNode = tmpNode;
			return true; 
		}
	}
	return false;
}

void increaseCountOf(WordList *aNode)
{
	aNode->count++;
}

WordList *getNewNode(const char *aWord)
{
	WordList *newNode;
	newNode = (WordList *) emalloc( sizeof(WordList));
	newNode->word = estrdup( aWord);
	newNode->count = 1;
	newNode->next=NULL;
	return newNode;
}

void printWordList(void)
{
	WordList *each;
	for( each = _startNode; each != NULL ; each = each->next){
		fprintf(stdout, "%s\t%d\n", each->word, each->count);
	}
}


///////////// End Of File //////////////////
