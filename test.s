section	.text
    global _start        ;must be declared for using gcc
	
_start:	      
    mov ecx, '9'
    mov eax, '1'
	
l1:
    mov [count], ecx

    mov [num], eax
    mov eax, 4
    mov ebx, 1
        
    mov ecx, num        
    mov edx, 1        
    int 0x80
        
    mov eax, [num]
    sub eax, '0'
    inc eax
    add eax, '0'
    
    mov eax, 4
    mov ebx, 1
    mov ecx, count
    mov edx, 1
    int 0x80

    dec ecx
    cmp ecx, 0
    jz l1
        
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, len
    int 0x80

    mov eax,1             ;system call number (sys_exit)
    int 0x80              ;call kernel

section .data
    msg db "END_", 0xa
    len equ $ - msg

section	.bss
num resb 1
count resb 10