section	.text
   global _start        ;must be declared for using gcc

_start:	                ;tell linker entry point

   mov     rsi, 4       ;pointing to the rightmost digit
   mov     rcx, 5       ;num of digits
   clc
add_loop:  
   mov 	al, [num1 + rsi]
   adc 	al, [num2 + rsi]
   aaa
   push
   or 	al, 30h
   pop
	
   mov	[sum + rsi], al
   dec	rsi
   loop	add_loop
	
   mov	rdx,len	        ;message length
   mov	rcx,msg	        ;message to write
   mov	rbx,1	        ;file descriptor (stdout)
   mov	rax,4	        ;system call number (sys_write)
   int	0x80	        ;call kernel
	
   mov	rdx,5	        ;message length
   mov	rcx,sum	        ;message to write
   mov	rbx,1	        ;file descriptor (stdout)
   mov	rax,4	        ;system call number (sys_write)
   int	0x80	        ;call kernel
	
   mov	rax,1	        ;system call number (sys_exit)
   int	0x80	        ;call kernel

section	.data
msg db 'The Sum is:',0xa	
len equ $ - msg			
num1 db '12345'
num2 db '23456'
sum db '     '