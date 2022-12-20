
; method reads whole line and returns content adn length
;
; RDI - output, pointer to start of string
; RSI - output, length
;
; affects RAX, RBX, RCX
readLine:

    mov rcx, 2 ; size
    call alloc
    mov rdi, rax
    mov rsi, rax

    readLineloadChar:
        read rsi, 1
        cmp [rsi], byte 0xa
        je readLineloadDone

        inc rsi
        cmp rsi, rbx
        jl readLineloadChar
            call alloc
            mov rax, rcx
            mov rcx, 2
            mul rcx
            mov rcx, rax

        jmp readLineloadChar
    readLineloadDone:
    mov [rsi], byte 0
    sub rsi, rdi
    ret

