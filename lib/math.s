addChar:
    sub rcx, byte "0"              
    mov rdx, 10
    mul rdx
    add rax, rcx