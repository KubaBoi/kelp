; rdx, char
%macro addCharToDecimal 2
sub [%2], byte "0"              
mov al, 10
mul %1
add %1, %2
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