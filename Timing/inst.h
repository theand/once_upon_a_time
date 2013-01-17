/*
 * inst.h
 */
#ifndef _INST_H_
#define _INST_H_

#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include "myutil.h"

#ifndef __cplusplus 
typedef int bool;
#endif

typedef struct clock_node{
	clock_t ticks;
	clock_t last_time;
	struct clock_node *next;
	char *name;
	bool clock_on;
}clock_type;

void start_clock(char *name);
void stop_clock(char *name);
void clock_report(void);

#endif

////////// End Of File /////////////////
