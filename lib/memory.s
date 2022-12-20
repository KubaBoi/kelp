
; method allocates bytes
;
; RCX - size of allocation in bytes
; RAX - output, pointer to start of memory
;
; affects RBX
alloc:
    mov rax, 45
    xor rbx, rbx
    int 80h

    add rax, rcx  ;number of bytes to be reserved
    mov rbx, rax
    mov rax, 45  ;sys_brk
    int 80h

    sub rax, rcx
    ret

; method allocates bytes and return address in RBX
;
; RCX - size of allocation in bytes
; RBX - output, pointer to start of memory
allocB:
    push rax
    call alloc
    mov rbx, rax
    pop rax
    ret