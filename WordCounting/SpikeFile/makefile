all : a.out

a.out : file.o myutil.o
	gcc -Wall file.o myutil.o
file.o : file.c
	gcc -c -Wall file.c
myutil.o : myutil.c myutil.h
	gcc -c -Wall myutil.c
