; using r.x because those are 64bit registers

section	.text
   global _start        ;must be declared for using gcc
	
_start:	                ;tell linker entry point
   call    display
   mov	rax,1	        ;system call number (sys_exit)
   int	0x80	        ;call kernel
	
display:
   mov    rcx, 256
	
next:
   push rcx
   mov     rax, 4
   mov     rbx, 1
   mov     rcx, achar
   mov     rdx, 1
   int     80h
	
   pop rcx	
   mov	dx, [achar]
   cmp	byte [achar], 0dh
   inc	byte [achar]
   loop    next
   ret
	
section .data
achar db '0'  