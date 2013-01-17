#include <stdio.h>

enum {MAX_NUMBER=10, NUM_ELEM=12};

void clearAllBits(unsigned char *aBit, int aTotalBitSize);
void setBit(unsigned char *aBit, int aNumber);
void printBit(unsigned char *aBit, int aBitIndex);
void test_setBit(unsigned char *aBit, int aRange);

int main(void)
{

	unsigned char bit[MAX_NUMBER]="TEST";

	int num[NUM_ELEM]={12,43,16,3,70,56,21,67,45,23,68,26};
	//~ 0 _ 1        _ 2  _ 3 _ 4 _ 5     _ 6 _  7  _ 8       _ 9 : array index 
	//0-7 8-15     16-23 24-31 32-39    40-47 48-55 56-63 64-71 : range by index
	//3 _ 12 _ 16 21 23 _ 26 _   _   _ 43 45 _    56 _ 67 68 70 : sorted number
	//16 _ 8        _ 133 _ 32 _ 0     _ 20 _ 0 _ 128 _ 26     _ 0 : array value
	
	int i;

	clearAllBits(bit,MAX_NUMBER);

	for(i=0; i<NUM_ELEM; i++)
		setBit(bit, num[i]);

	for(i=0; i<MAX_NUMBER; i++)
		printBit(bit,i);
	printf("\n");

	return 0;
}


void test_setBit(unsigned char *aBit, int aRange)
{
	int i;

	for(i=0;i<aRange;i++){
		setBit(aBit,i);
		printf("%d - %d\n", i,aBit[i/8]);
		aBit[i/8]=0;
	}
}

void clearAllBits(unsigned char *aBit, int aTotalBitSize)
{
	//TODO: bit 별로 clear 하는 걸 만들어야겠다.
	int i;

	for(i=0;i<aTotalBitSize;i++)
		aBit[i]=0;
}

void setBit(unsigned char *aBit, int aNumber)
{
	unsigned char mask[]={128,64,32,16,8,4,2,1};

	aBit[aNumber/8]=aBit[aNumber/8] | mask[aNumber%8];
#ifdef DEBUG
	printf("%d - %d - %d - %d\n", aNumber , aNumber/8, aNumber%8, aBit[aNumber/8]);
#endif
}

void printBit(unsigned char *aBit, int aBitIndex)
{
	int i;
	unsigned char mask[]={ 128,64,32,16,8,4,2,1};

#ifdef DEBUG
	printf("%d--", aBitIndex);
#endif 
	for(i=0; i<8; i++)
		if( (aBit[aBitIndex] & mask[i]) == mask[i])
			printf("%d  ", 8*aBitIndex+i);
	//printf("\n");


}
