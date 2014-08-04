
all: hello.so

hello.so: hello.o
	gcc -shared $< -o $@

hello.o: hello.c
	gcc -Wall -c $< -o $@
