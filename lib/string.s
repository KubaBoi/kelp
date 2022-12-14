

; method converts decimal value stored in RAX
; to string and puts it inside [RBX] 
; 
; RAX - input, integer
; RBX - output, pointer to char*
; RSI - output, integer, length of string
;
; affects RAX, RCX, RDX, RSI
toString:
    mov rcx, 10 ; delitel
    push rax
    call decCharCnt
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
    inc rbx
    inc rsi
    ret

; method counts char size of decimal number
;
; RAX - input, decimal number
; RSI - output, count
;
; affects RAX, RCX, RDX
decCharCnt:
    xor rsi, rsi
    mov rcx, 10
    decCharCountLoop:
        xor rdx, rdx
        idiv rcx
        inc rsi
        cmp rax, 0
        jg decCharCnt
    ret

; method counts string length if ending with 0
;
; RBX - string address
; RSI - output, length
;
strLen:
    mov rsi, rbx
    strLenLoop:
        cmp [rsi], byte 0
        jz strLenDone
        inc rsi
        jmp strLenLoop
    strLenDone:

    sub rsi, rbx
    ret