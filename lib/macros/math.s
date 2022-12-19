;import stack.s

; rdx, char
%macro addCharToDecimal 0
sub rdx, byte "0"              
mov rcx, 10
mul rcx
add rax, rdx
%endmacro

%macro isNumber 1
cmp %1, byte 0xa
je isNumberex
cmp %1, byte ":"
jge numberError
cmp %1, byte "0"
jl numberError
isNumberex:
%endmacro
