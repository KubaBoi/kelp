;import lib/macros/io.s

section	.text
   global _start         ;must be declared for using gcc
	
;import lib/string.s
;import lib/memory.s
;import lib/io.s


sqrt:
    mov rbx, rax
    mov rcx, rax
    xor rdx, rdx
    sqrtLoop:
        mul rbx
        dec rcx
        jz sqrtEndLoop
        jmp sqrtLoop
    sqrtEndLoop:
    ret

_start:	                 ;tell linker entry point

    mov rax, 3
    call sqrt

    br:
    push rax
    mov rcx, 20
    call alloc
    mov rbx, rax
    pop rax
    call toString
    mov rdi, rbx
    print rdi, rsi

    mov rbx, msg
    call strLen
    print msg, rsi

    call readLine
    print rdi, rsi

exit:
    mov	rax, 1
    xor	rbx, rbx
    int	80h
	
section	.data
msg db "Write a word: ", 0 ; 14
msg2 db "Next? [y/n] ", 0 ; 12

names dw 0
namesSize dw 1