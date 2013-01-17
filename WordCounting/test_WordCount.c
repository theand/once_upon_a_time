
/*
 * test_WordCounting.c
 * - 단어, 라인, 문자 수 카운트 유닛 테스트
 * */

#include <stdio.h>
#include "wc.h"

int main(void)
{
	int numOfWord;
	int numOfLine;
	int numOfChar;

	char sample[]="\tHello World	Tab\n\nNew,Line.Dot:Colon;SemiColon<Lessthan>greaterthen[leftbracket]RightBracket&Ampersand%Percent\t\n";
	char aLine[]="asdf\n";
	char notALine[]="asdf";
	char newLine [] = "abcde\nf.gh i, kl";

	numOfWord = countWord(sample);
	assert(numOfWord==14);

	numOfLine = countLine(aLine);
	assert(numOfLine==1);

	numOfLine = countLine(notALine);
	assert(numOfLine==0);

	numOfLine = countLine(sample);
	assert(numOfLine==3);

	numOfChar = countChar(aLine);
	assert(numOfChar==4);

	numOfChar = countChar(newLine);
	assert(numOfChar==11);

	setPrintMode(7); 
	printResult();
	return 0;
}

	
///////////////////// End Of File ///////////////////////
