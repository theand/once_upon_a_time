#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

enum {StackMax =60};


char _stack[StackMax];
int _top = -1;

int i, j;

int pushStack(char symbol);
char popStack(void);
int getPrecedence(int symbol);
void infix2prefix(char *aTarget, char aSrc[]);
void flushStackTo(char *aTarget );
int getStackTop(void);
void putExprTo(char **aTarget);

int main(void)
{

	char preexpr[StackMax];
	char inexpr[StackMax];

	printf("수식을 입력하세요 : ");
	scanf("%s", inexpr);
	i = strlen(inexpr) - 1;

	infix2prefix(preexpr, inexpr);

	for (j = strlen(preexpr) - 1; j >= 0; j--)
		printf("%c", preexpr[j]);
	printf("\n");

	return 0;

}

int pushStack(char symbol)
{
	_top++;

	if (_top > StackMax) {
		printf("\nStack is full");
		exit(-1);
	}
	_stack[_top] = symbol;
	return 1;

}

char popStack(void)
{

	if (_top < 0)
		return -1;

	return _stack[_top--];

}

void flushStackTo(char *aTarget )
{
	while (_top >= 0) {
		//putExprTo(&aTarget);
		*aTarget++ = popStack();
		*aTarget++ = ' ';
	}
	aTarget--;
	*aTarget = 0;

}
int getStackTop(void)
{
	assert(_top>=0);
	assert(_top<StackMax);
	return _stack[_top]; 
}

/*
void putExprTo(char **aTarget)
{
	*aTarget++ = popStack();
	*aTarget++ = ' ';
}

 */

int getPrecedence(int symbol)
{

	switch (symbol) {
	case ')':
		return 0;
	case '+':
	case '-':
		return 1;
	case '*':
	case '/':
	case '%':
		return 2;
	default:
		return 3;
	}

}
void infix2prefix(char *preexpr, char inexpr[])
{

	while (i >= 0) {
		if (inexpr[i] == ')') {
			pushStack(inexpr[i]);
			i--;
		} else if (inexpr[i] == '(') {
			while (getStackTop() != ')') {
				*preexpr++ = popStack();
				*preexpr++ = ' ';
			}
			popStack();
			i--;
		} else if (strchr("+-*/%", inexpr[i]) != 0) {
			while (_top >= 0
				   && getPrecedence(getStackTop()) >=
				   getPrecedence(inexpr[i])) {
				*preexpr++ = popStack();
				*preexpr++ = ' ';
			}
			pushStack(inexpr[i]);
			i--;
		} else if (isalnum(inexpr[i])) {
			do {
				*preexpr = inexpr[i];
				*preexpr++;
				i--;
			} while (isalnum(inexpr[i]));

			*preexpr++ = ' ';
		} else
			i--;
	}

	flushStackTo(preexpr);


}



////////////////// EOF ////////////////////////
