save:
    push rax
    push rbx
    push rcx
    push rdx
    ret

load:
    pop rdx
    pop rcx
    pop rbx
    pop rax
    ret
    