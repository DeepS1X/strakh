# compiler for C program
CC = gcc

# compiler flags:
#  -g    adds debugging info a.out
#  -Wall turns on most compiler warnings
CFLAGS  = -g -Wall -Werror -static -fPIE -fstack-protector-all -D_FORTIFY_SOURCE=2 -Wl,-z,now -Wl,-z,relro

default:

whoami: tricks/whoami.c
	$(CC) $(CFLAGS) tricks/whoami.c -o tricks/whoami && chmod +x tricks/whoami

id: tricks/id.c
	$(CC) $(CFLAGS) tricks/id.c -o tricks/id && chmod +x tricks/id
