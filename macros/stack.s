%macro save 0
push rax
push rbx
push rcx
push rdx
%endmacro

%macro load 0
pop rdx
pop rcx
pop rbx
pop rax
%endmacro