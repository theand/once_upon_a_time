
/*
 * wc.h
 * */

#ifndef _WC_H_
#define _WC_H_

#include <stdio.h>
#include <assert.h>
#include "myutil.h"
#ifdef _ARRAY_
#include "array.h"
#else
#include "list.h"
#endif


void handleArgument(int argc, char **argv);

void setPrintMode(int mode);
void printResult(void);

int getNumOfWords(void);
int getNumOfChars(void);
int getNumOfLines(void);

void setFileName(char *name);
char *getFileName(void);

char *getLine(void); 
void initLineList(void);
int hasNextLine(void);

int countWord(const char *aLine);
int countLine(const char *aLine);
int countChar(const char *aLine);


#endif



///////////////////// End Of File ////////////////////////
