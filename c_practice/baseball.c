/*
	gcc baseball.c
	이걸로 컴파일하고 ./a.out 으로 실행.

	gcc -DDEBUG baseball.c 
	이걸로 컴파일하면 디버그 모드라서 답을 미리 볼수있음.
	실행은 똑같이.
*/

#include <stdio.h>
#include <stdlib.h>//rand()
#include <time.h>
#include <assert.h>

//this macro evaluate the number of array elements
#define num_of(array) (sizeof(array)/sizeof(array[0])) 

enum{diff=0,same=1,true=1,false=0};//compile time 상수

void generateNum(char *rightAns);
void getNum(char *myAns);
int compNum(char *rightAns, char *myAns);
int isCont(void);

int main(void)
{
	char rAns[4];
	char myAns[4];

	do{
		generateNum(rAns);
		do{
			getNum(myAns);
		} while( compNum(rAns, myAns)==diff) ;//compare two number.
	}while( isCont()==true );//to continue or not to coninue

	return 0;
}

int isCont(void)
{
	char c;
	
	do{
	fflush(stdin);
	printf("Do you want to continue game?(y/n)");
	scanf("%c",&c);
	}while( c!='y' && c!='n' );

	if( c == 'y')
		return true;
	else
		return false;
}

int compNum(char *rightAns, char *myAns)
{
	int s=0;//strike counter
	int b=0;//ball counter
	int i,j;//loop index

	assert( rightAns!=NULL );
	assert( myAns!=NULL );

	for( i=0; i<3 ;i++ )
		for( j=0; j<3 ; j++ )
			if( rightAns[i] == myAns[j] ){
				if( i==j )
					s++;
				else 
					b++;
				break;
			}//inner for

	if( s!=0 && b ==0 )//no ball
		printf("%d strikes\n", s);
	else if( s!=0 && b!=0 )//both strike and ball
		printf("%d strikes %d balls\n", s,b);
	else if( s==0 && b!=0 )//no strike
		printf("%d balls\n", b);
	else//no count
		printf("Out!\n");

	if( s==3 ){//if three strikes
		printf("Congratulations~! You're right!\n");
		return same;
	}
	else
		return diff;
}

void getNum(char *myAns)
{
	assert(myAns!=NULL);
	printf("Input numner :");
	scanf("%3s", myAns);
	fflush(stdin);//flush buffer

	//TODO: isCorrect();
}

void generateNum(char *rightAns)
{
	int n=0;//generated number( 1~9 )
	int c=0;//count
	int table[10];//table[0] 은 dummy space. 
				  //테이블에 해당 번호가 이미 나왔는지 아닌지 플래그를 둔다.
				  //1~9 까지만 유효하다.
	long int r;//

	assert(rightAns!=NULL);

	srand(time(NULL));

	for( c=0; c < num_of(table); c++)
		table[c]=false;//initialize

	for( c=0; c < 3 ; c++ ){
		while( 1 ){
			r = rand();//generate random number
			n = r%10;//maybe n is 0~9

			if( n==0 || table[n]==true )//0 is not allowed, or duplicated number
				continue;//re-generate another number

			//now, n is must 1~9 with do duplication.
			rightAns[c]=n+'0';
			table[n]=true;//flag set.
			break;

		}//end of while

		n=0;//table[0] is always 0.

	}//end of for

	rightAns[c]='\0';//c is 3(the last index). mark '\0'. because it is string.

#ifdef DEBUG
	printf("Right Answer is %s\n", rightAns);
#endif
}
