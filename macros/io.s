;import stack.s

%macro print 2
save
mov	rax, 4 
mov	rbx, 1
mov	rcx, %1
mov	rdx, %2
int	80h		 ;print a message
load
%endmacro

; [buffer], lenght
%macro read 2           
save
mov rax, 3
mov rbx, 2
mov rcx, %1
mov rdx, %2         ;5 bytes (numeric, 1 for sign) of that information
int 80h
load
%endmacro