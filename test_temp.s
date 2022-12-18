
%macro save 0
push rax
push rbx
push rcx
push rdx
%endmacro

%macro load 0
pop rdx
pop rcx
pop rbx
pop rax
%endmacro


; rdx, char
%macro addCharToDecimal 2
sub [%2], byte "0"              
mov al, 10
mul %1
add %1, %2
%endmacro

%macro isNumber 1
cmp %1, byte 0xa
je isNumberex
cmp %1, byte ":"
jge numberError
cmp %1, byte "0"
jl numberError
isNumberex:
%endmacro



%macro print 2
save
mov	rax, 4 
mov	rbx, 1
mov	rcx, %1
mov	rdx, %2
int	80h		 ;print a message
load
%endmacro

; [buffer], lenght
%macro read 2           
save
mov rax, 3
mov rbx, 2
mov rcx, %1
mov rdx, %2         ;5 bytes (numeric, 1 for sign) of that information
int 80h
load
%endmacro


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
    mov rax, 12;
    call toString
    print rbx, count

    jmp exit


toString:
    xor edi, edi
    toStringLoop:
        ;rax ; delenec
        xor rdx, rdx  ; zbytek
        mov rcx, 10 ; delitel
        cqo
        idiv rcx

        mov bl, byte "0"
        mov [char], byte "0"
        add [bl], rdx
        add [char], rdx
        print char, 1
        inc edi

        cmp rax, 0
        jg toStringLoop
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
    sumStr times count db 0

section .bss
    sum resb 5


