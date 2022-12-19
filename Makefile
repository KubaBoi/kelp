
# MAKEFILE GENERATED BY PTT
# https://github.com/KubaBoi/ptt

NAME=test.s_temp
OBJFILES=$(NAME).o 

CC=nasm
CFLAGS= 

%.o : %.c 
	$(CC) $(CFLAGS) -c $<

all: $(NAME)

dep:
	$(CC) -MM *.c >dep.list

-include dep.list

$(NAME): $(OBJFILES)
	$(CC) $(CFLAGS) $(OBJFILES) -o $@
	