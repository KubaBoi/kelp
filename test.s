
;import macros/stack.s
;import macros/math.s
;import macros/io.s

section	.text
   global _start         ;must be declared for using gcc
	
_start:	                 ;tell linker entry point
    
    mov rbx, 0;12345678912345678912
    jmp ex
    loadLoop:
        print msg1, len1
        mov rdx, 0
        mov [char], byte "0"
        loadChar:
            addCharToDecimal rdx, char
            read char, 1
            isNumber [char]
            cmp [char], byte 0xa
            jne loadChar

        add rbx, rdx

        print msg4, len4
        read char, 2
        cmp [char], byte "y"
        je loadLoop 

    ;toString
    ;print sumStr, count

ex:
    mov rax, 12
    mov rbx, sumStr
    call toString
    print sumStr, count

    jmp exit


toString:
    mov rcx, 10 ; delitel
    toStringLoop:
        ;rax ; delenec
        xor rdx, rdx  ; zbytek
        idiv rcx

        mov [rbx], byte "0"
        add [rbx], rdx
        inc rbx

        cmp rax, 0
        jg toStringLoop
        mov [rbx], byte 0
    ret

numberError:
    print msg2, len2
    jmp exit

lengthError:
    print msg3, len3
    jmp exit

exit:
    mov	rax, 1
    int	80h
	
section	.data
    msg1 db "Enter number: ", 0
    len1 equ $ - msg1

    msg2 db "Not a number.", 0xa, 0
    len2 equ $ - msg2

    msg3 db "Too long.", 0xa, 0
    len3 equ $ - msg3

    msg4 db "More? [y/n] ", 0
    len4 equ $ - msg4

    char db 0

    count equ 20
    sumStr db 12
    ;sumStr times count db 0
    

section .bss
    sum resb 5
