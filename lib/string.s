

; method converts decimal value stored in RAX
; to string and puts it inside [RBX] 
; 
; RAX - integer
; RBX - pointer to char*
;
; affects RAX, RCX, RDX
toString:
    mov rcx, 10 ; delitel
    push rax
    call charSize
    pop rax
    add rbx, rsi
    mov [rbx], byte 0
    toStringLoop:
        ;rax ; delenec
        xor rdx, rdx  ; zbytek
        idiv rcx

        mov [rbx], byte "0"
        add [rbx], rdx
        dec rbx

        cmp rax, 0
        jg toStringLoop
    ret

; method counts char size of decimal number
;
; RAX - decimal number
; RSI - output, count
;
; affects RAX, RCX, RDX
charSize:
    xor rsi, rsi
    mov rcx, 10
    charSizeLoop:
        xor rdx, rdx
        idiv rcx
        inc rsi
        cmp rax, 0
        jg charSizeLoop
    ret