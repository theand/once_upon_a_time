
#include "list.h"
#include "myutil.h"


int main(void)
{
	/*
	WordList *Start;
	Start = (WordList *) emalloc( sizeof(WordList) );
	Start->word = estrdup("Word");
	Start->count = 3;
	assertStrEquals( Start->word, "Word");
	assertEquals( Start->count, 3);

	Start->next = (WordList *) emalloc( sizeof(WordList) );
	Start->next->word = estrdup("Wod");
	Start->next->count = 1;
	assertStrEquals( Start->next->word, "Wod");
	assertEquals( Start->next->count, 1);*/

	assertTrue( StrLess("List", "Word") );
	insertWord("Word");
	assertStrEquals( "Word", _startNode->word);
	assertEquals(1,_startNode->count);
	assertTrue( isInclude("Word") );

	insertWord("List");
	assertStrEquals( "List", _startNode->word);
	assertEquals(1,_startNode->count);

	insertWord("ABC");
	assertStrEquals( "ABC", _startNode->word);
	assertEquals(1,_startNode->count);

	insertWord("ABD");
	assertStrEquals( "ABD", _startNode->next->word);
	assertEquals(1,_startNode->next->count);

	insertWord("XYZ");
	assertTrue( isInclude("XYZ") );
	assertStrEquals( "XYZ", _lastNode->word);
	insertWord("XYZ");
	assertTrue( isInclude("XYZ") );
	assertEquals(2,_lastNode->count);
	/*
	insertWord("Fourth");
	assertStrEquals( "Fourth", _startNode->next->next->word);
	assertEquals(1,_startNode->next->next->count);

	insertWord("Word");
	assertStrEquals( "Word", _startNode->word);
	assertEquals(2,_startNode->count);

	insertWord("Word");
	assertTrue( isInclude("Word") );
	assertStrEquals( "Word", _startNode->word);
	assertEquals(3,_startNode->count);
	 */

	assertFalse( isInclude("Non") );

	//printWordList();
	return 0;
}

