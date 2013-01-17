CC=gcc 
OPTION=-Wall -g -D_LIST_
#OPTION=-DNDEBUG

all : list
	ctags *.c *.h

######################
test_wc : test_wc.o myutil.o wc.o 
	$(CC) test_wc.o myutil.o wc.o  -o test $(OPTION)

test_wc.o : test_wc.c
	$(CC) -c test_wc.c $(OPTION)

test_unit : test_WordCount.o myutil.o wc.o
	$(CC) test_WordCount.o myutil.o wc.o  -o twc $(OPTION)

test_WordCounting.o : test_WordCount.c
	$(CC) -c test_WordCount.c $(OPTION)

test_print : test_pr.o myutil.o wc.o array.o
	$(CC) test_pr.o myutil.o wc.o array.o  -o test_pr $(OPTION)

test_pr.o : test_pr.c 
	$(CC) -c test_pr.c $(OPTION)

test_list : test_list.o myutil.o list.o
	$(CC) test_list.o myutil.o  list.o  -o test_list $(OPTION)

test_list.o : test_list.c 
	$(CC) -c test_list.c $(OPTION)

################
array : main.o myutil.o wc.o array.o
	$(CC) main.o myutil.o wc.o array.o $(OPTION)

list : main.o myutil.o wc.o list.o
	$(CC) main.o myutil.o wc.o list.o $(OPTION)

array.o : array.c array.h
	$(CC) -c array.c $(OPTION)

list.o : list.c list.h
	$(CC) -c list.c $(OPTION)

main.o : main.c
	$(CC) -c main.c $(OPTION)

myutil.o : myutil.c myutil.h
	$(CC) -c myutil.c $(OPTION)

wc.o : wc.c wc.h
	$(CC) -c wc.c $(OPTION)

clean : 
	rm -f a.out *.o core 

