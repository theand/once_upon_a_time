/*
 * inst.c
 */

#include "inst.h"


clock_type *clock_head = NULL;

void start_clock(char *aName)
{
	clock_type *p;
	for(p = clock_head; p!=NULL; p=p->next)
		if( StrEqual(p->name, aName) )
			break;
	if( p == NULL ){
		p = (clock_type *) emalloc (sizeof(struct clock_node));
		p->name = estrdup(aName);
		p->ticks = 0;
		p->next = clock_head;
		p->clock_on = true;
		clock_head = p;
	}
	else if( p->clock_on ){
		fprintf( stderr, "Error: clock '%s' already on\n", aName);
		return;
	}
	p->clock_on=true;
	p->last_time = clock();
}

void stop_clock(char *aName)
{
	clock_t ticks = clock();
	clock_type *p;
	for(p = clock_head; p!=NULL; p=p->next)
		if( StrEqual(p->name, aName) )
			break;
	if( p == NULL ){
		fprintf(stderr, "Error : Clock '%s' not found\n", aName );
		return;
	}
	else if( !p->clock_on )
		fprintf( stderr, "Error : Clock '%s' not started\n", aName);
	p->clock_on = false;
	p->ticks += ticks - p->last_time;
}

void clock_report(void)
{
	clock_type *p;
	clock_t total = clock();
	fprintf( stderr, "--------------- Clock Profile ---------------\n");
	for( p = clock_head; p != NULL; p=p->next){
		if( p->clock_on )
			fprintf( stderr, "Error : Clock '%s' not stopped\n", p->name);
		fprintf(stderr, "Clock '%s' %5.2f secs, %5.2f%%\n", p->name, p->ticks / (double) CLOCKS_PER_SEC, p->ticks / (double) total*100.0 );
	}
	free(p);
	//TODO : memory leak?
}


////////// End Of File //////////////
