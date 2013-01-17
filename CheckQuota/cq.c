//
// find the user who use storage too much
//
// USAGE : 
// 	./check [MAX USAGE SIZE(MB)]
//

#include<stdio.h>
#include<string.h>

int main(char args, char **argv)
{
	char buffer[255], studentNumber[255];
	short int usage, MAX_USAGE;
	FILE *fp;

	system("du -sm /home/under/* > du.history");
	fp = fopen("./du.history", "r");
	if(!fp) {
		fprintf(stderr, "Error: Can't open history file.\n");
	}	
	
	if(args == 1) {
		MAX_USAGE = 100;
	} else {
		MAX_USAGE = atoi(argv[1]);
	}

	while(fgets(buffer, 255, fp)) {
		if(strlen(buffer) == 0)
			break;
		sscanf(buffer, "%d %s", &usage, studentNumber);
		if(usage > MAX_USAGE) {
			printf("%s : %d MB\n", studentNumber, usage);
		}
	}
	return 0;
}
