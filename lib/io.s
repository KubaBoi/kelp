
; method reads whole line and returns content adn length
;
; RSI - pointer to start of string
; RDI - length
;
; affects RAX, RBX, RCX
readLine:

    mov rcx, 2 ; size
    call alloc
    mov rdi, rax
    mov rsi, rax

    readLineloadChar:
        read rdi, 1
        cmp [rdi], byte 0xa
        je readLineloadDone

        inc rdi
        cmp rdi, rbx
        jl readLineloadChar
            call alloc
            mov rax, rcx
            mov rcx, 2
            mul rcx
            mov rcx, rax

        jmp readLineloadChar
    readLineloadDone:
    mov [rdi], byte 0
    sub rdi, rsi
    ret
