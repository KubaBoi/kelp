section	.text
    global _start        ;must be declared for using gcc
	
_start:	      
    mov [c], word 10
    mov eax, '1'
	
l1:
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
    
    dec word [count]
    jnz l1
        
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, len
    int 0x80

    mov eax,1             ;system call number (sys_exit)
    int 0x80              ;call kernel

section .data
    msg db 0xa, "END_", 0xa
    len equ $ - msg

section	.bss
    num resb 1
    c resb 1 ; tady bacha na resw... 