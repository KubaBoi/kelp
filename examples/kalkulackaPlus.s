section	.text
   global _start        ;must be declared for using gcc

_start:	                ;tell linker entry point
   mov     esi, 4       ;pointing to the rightmost digit
   mov     ecx, 5       ;num of digits
   clc

add_loop:  
   mov 	al, [num1 + esi]
   add 	al, [num2 + esi]
   add al, [m]
   sub al, byte "0"
   mov [m], byte 0

   cmp al, 58 ; ":"
   jl cont
   mov [m], byte 1
   sub al, byte 10

      cont:
   mov [sum + esi], al
   dec	esi
   loop	add_loop

   mov	edx,5	        ;message length
   mov	ecx,sum	        ;message to write
   mov	ebx,1	        ;file descriptor (stdout)
   mov	eax,4	        ;system call number (sys_write)
   int	0x80	        ;call kernel

   mov	eax,1	        ;system call number (sys_exit)
   int	0x80	        ;call kernel

section	.data
num1 db '12345', 0xa
num2 db '23435', 0xa
sum0 db '35801', 0xa

m db 0
sum db '     ' ; 35801