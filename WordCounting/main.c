/*------------------------------------------------ 
 * main.c
 * ------------------------------------------------*/ 

#include "myutil.h"
#include "wc.h"
#ifdef _ARRAY_
#include "array.h"
#else
#include "list.h"
#endif


int main(int argc, char **argv)
{

	char *line;
	int isPrintList = true;//TODO

	setProgName("Word Counting"); 
	handleArgument(argc, argv);
	setPrintMode(7);

	initLineList();

	printf("filename = %s\n", getFileName() );
	while( hasNextLine() == true ){
		line = getLine();
		countWord( line );
		countLine( line );
		countChar( line );
	}

	printResult();
	if( isPrintList )
		printWordList();
	return 0;
}

//////////////////////   End Of File  ///////////////////
