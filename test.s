%macro print 2
mov	eax, 4
mov	ebx, 1
mov	ecx, %1
mov	edx, %2
int	80h		 ;print a message
%endmacro

%macro read 2
mov eax, 3
mov ebx, 2
mov ecx, %1 
mov edx, %2          ;5 bytes (numeric, 1 for sign) of that information
int 80h
%endmacro

%macro isNumber 1
cmp [%1], byte ":"
jge error
cmp [%1], byte "0"
jl error
%endmacro

section	.text
   global _start         ;must be declared for using gcc
	
_start:	                 ;tell linker entry point
    print msg1, len1
    read num1, 5
    isNumber num1

    print msg1, len1
    read num2, 5
    isNumber num2

    mov al, [num1]
    sub al, "0"
    add al, [num2]

    mov [sum], al

    print sum, 1

    jmp exit

error:
    print msg2, len2

exit:
    mov	eax, 1
    int	80h
	
section	.data
    msg1 db "Enter number:", 0xa
    len1 equ $ - msg1

    msg2 db "Need to be number.", 0xa
    len2 equ $ - msg2

    sum db " ", 0

section .bss
    num1 resb 5
    num2 resb 5
