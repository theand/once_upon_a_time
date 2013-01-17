#include <stdio.h>
#include "myutil.h"

int array[6];

void print(void)
{
	int i;
	for(i=0;i<6;i++)
		printf("%d\n", array[i]);
}
int hasNextLine(FILE *fp)
{
	return feof(fp)==0;
}
int main(void)
{
	FILE*fp;
	char temp[20];
	int i=0;

	fp = efopen("sample.dat", "r");

	while(hasNextLine(fp)){
		//fgets(temp, 19, fp);
		sscanf(fp, "%d %d", &array[i], &array[i+1]);
		i=i+2;
	}

	print();

	return 0;
}

