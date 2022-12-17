
;import macros/stack.s
;import macros/math.s
;import macros/io.s

section	.text
   global _start         ;must be declared for using gcc
	
_start:	                 ;tell linker entry point
    
    mov bx, 157
    jmp toStringLoop
    loadLoop:
        print msg1, len1
        mov dx, 0
        mov [char], byte "0"
        loadChar:
            ;addCharToDecimal dx, char
            read char, 1
            isNumber [char]
            cmp [char], byte 0xa
            jne loadChar
        add bx, dx

        print msg4, len4
        read char, 2
        cmp [char], byte 'y'
        je loadLoop 

    toStringLoop:
        mov ax, bx
        cwd
        mov cx, 10
        idiv cx
        imul cx
        mov dx, ax
        sub dx, bx

        mov [char], byte "0"
        sub [char], dx
        print char, 1

        sub ax, dx
        idiv cx
        mov bx, ax
        cmp bx, 0
        jg toStringLoop
        ;mov [char], byte "0"
        ;sub [char], ax
        ;print char, 1

    jmp exit

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

    char db "0"

    count equ 100
    sumStr times count db 0

section .bss
    sum resb 5
