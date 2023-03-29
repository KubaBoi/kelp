
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

; RAX - input, integer, rooted number
; RBX - input, integer, root number
;
; RAX - output, integer, result
;
; affects RCX, RDX
sqrt:
    xor rdx, rdx
    mov rcx, rax
    sqrtLoop:
        dec rbx
        jle sqrtEndLoop
        mul rcx
        jmp sqrtLoop
    sqrtEndLoop:
    ret