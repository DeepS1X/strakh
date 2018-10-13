# compiler for C program
CC = gcc

# compiler flags:
#  -g    adds debugging info a.out
#  -Wall turns on most compiler warnings
CFLAGS  = -g -Wall -Werror

whoami: tricks/whoami.c
	$(CC) $(CFLAGS) tricks/whoami.c -o tricks/whoami && chmod +x tricks/whoami
