/*
 * test_wc.c
 * �����б� �׽�Ʈ
 * */
#include <stdio.h>
#include "wc.h"

int main(void)
{
	setFileName("sample.txt");
	setPrintMode(7);
	printResult();
	printf("filename = %s\n", getFileName() );
	initLineList();
	while( hasNextLine() == true )
		printf("%s\n", getLine() );
	return 0;
}

	
///////////// End Of File /////////////////////
