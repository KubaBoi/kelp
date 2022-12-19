

; method converts decimal value stored in RAX
; to string and puts it inside [RBX] 
; 
; RAX - integer
; RBX - pointer to char*
;
; affects RCX and RDX
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