;import lib/macros/io.s

section	.text
   global _start         ;must be declared for using gcc
	
;import lib/string.s
;import lib/memory.s
;import lib/io.s
;import lib/math.s

; RAX - input, integer, rooted number
; RBX - input, integer, root number
;
; RAX - output, integer, result
;
; affects RCX, RDX
sqrt:
    xor rdx, rdx
    mov rcx, rax
    sqrtLoop:
        dec rbx
        jle sqrtEndLoop
        mul rcx
        jmp sqrtLoop
    sqrtEndLoop:
    ret

readNumber:
    mov rax, 0
    push rax
    call readLine   ; rdi
    pop rax
    readNumberLoop:
        mov rcx, 20
        call allocB     ; rbx
        mov rcx, [rdi]
        call addCharToDecimal ; 
        inc rdi
        mov rcx, rsi
        add rcx, rdi
        cmp rdi, rcx
        jl readNumberLoop
    ret

_start:	                 ;tell linker entry point

    call readNumber

    mov rcx, 20
    call allocB

    call toString
    mov rdi, rbx
    print rdi, rsi

    print break, 1

    mov rbx, 1
cyklus:
    push rbx
    mov rax, 3
    call sqrt

    mov rcx, 20
    call allocB
    call toString
    mov rdi, rbx
    print rdi, rsi
    print break, 1
    pop rbx
    inc rbx
    cmp rbx, 10
    jl cyklus


    ;mov rbx, msg
    ;call strLen
    ;print msg, rsi

    ;call readLine
    ;print rdi, rsi

exit:
    mov	rax, 1
    xor	rbx, rbx
    int	80h
	
section	.data
break db 0xa
msg db 0xa, "Write a word: ", 0 ; 14
msg2 db "Next? [y/n] ", 0 ; 12

names dw 0
namesSize dw 1