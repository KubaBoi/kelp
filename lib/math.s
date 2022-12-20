
; method adds <0-9> number as char to decimal
;
; RAX - decimal
; RCX - intput, char
; 
; affects RDX
addCharToDecimal:
    sub rcx, byte "0"              
    mov rdx, 10
    mul rdx
    add rax, rcx
    ret

; 