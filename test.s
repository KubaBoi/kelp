;import lib/macros/io.s

section	.text
   global _start         ;must be declared for using gcc
	
;import lib/string.s
;import lib/memory.s
;import lib/io.s


_start:	                 ;tell linker entry point

    mov rbx, msg
    call strLen
    print msg, rsi

    call readLine
    print rsi, rdi

exit:
    mov	rax, 1
    xor	rbx, rbx
    int	80h
	
section	.data
msg db "Write a word: ", 0 ; 14
msg2 db "Next? [y/n] ", 0 ; 12

names dw 0
namesSize dw 1