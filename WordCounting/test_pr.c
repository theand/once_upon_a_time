
/*
 * test_pr.c
 * 단어 저장 유닛 테스트
 * */
#include <stdio.h>
#include "myutil.h"
#include "wc.h"


int main(void)
{

	insertWord("Word");
	assertStrEquals("Word", getNodeAt("Word")->word );
#ifdef DEBUG
	printf("%s\n", getNodeAt("Word")->word );
#endif 

	assertTrue( isInclude("Word") );

	insertWord("List");
	assertTrue( StrEqual("List", getNodeAt("List")->word) );
	assertTrue( isInclude("List") );

	insertWord("Print");
	assertTrue( StrEqual("Print", getNodeAt("Print")->word) );

	insertWord("Print");

	insertWord("Word");
	assertEquals( 2 , getOccurrenceOf("Word") );


	assertFalse( isInclude("Non") );

	assertEquals( 2 , getIndexOf("Print") );

	return 0;
}


//////////////////////////// End Of File //////////////////////
