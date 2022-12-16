; Flags
; OF            Overflow
; DF            Direction
; IF            Interrupt
; TF            Trap
; SF            Sign
; ZF            Zero
; AF            Auxiliary
; PF            Parity
; CF            Carry


; signed
; JE/JZ         Equal - Zero                ZF
; JNE/JNZ       not Equal - not Zero        ZF  
; JG/JNLE       Greater - not Less/Equal    OF, SF, ZF
; JGE/JNL       Greater/Equal - not Less    OF, SF
; JL/JNGE       Less - not Greater/Equal    OF, SF
; JLE/JNG       Less/Equal - not Greater    OF, SF, ZF

; unsigned
; JE/JZ         Equal - Zero                ZF
; JNE/JNZ       not Equal - not Zero        ZF
; JA/JNBE       Above - not Below/Equal     CF, ZF
; JAE/JNB       Above/Equal - not Below     CF
; JB/JNAE       Below - not Above/Equal     CF
; JBE/JNA       Below/Equal - not Above     AF, CF

; check value of flags
; JXCZ          if CX is Zero               none
; JC            if Carry                    CF
; JNC           if not Carry                CF
; JO            if Overflow                 OF
; JNO           if not Overflow             OF
; JP/JPE        if Parity or Parity Even    PF
; JNP/JPO       if no Parity or Parity Odd  PF
; JS            Sign (negative value)       SF
; JNS           No Sign (positive value)    SF

section	.text
    global _start         ;must be declared for using gcc

_start:	                 ;tell linker entry point
    mov   ecx, [num1]
    cmp   ecx, [num2]
    jg    check_third_num
    mov   ecx, [num2]
   
check_third_num:

    cmp   ecx, [num3]
    jg    _exit
    mov   ecx, [num3]
   
_exit:
   
    mov   [largest], ecx
    mov   ecx,msg
    mov   edx, len
    mov   ebx,1	;file descriptor (stdout)
    mov   eax,4	;system call number (sys_write)
    int   0x80	;call kernel
        
    mov   ecx,largest
    mov   edx, 2
    mov   ebx,1	;file descriptor (stdout)
    mov   eax,4	;system call number (sys_write)
    int   0x80	;call kernel
        
    mov   eax, 1
    int   80h

section	.data
   
    msg db "The largest digit is: ", 0xA,0xD 
    len equ $- msg 
    num1 dd '47'
    num2 dd '22'
    num3 dd '31'

segment .bss
   largest resb 2  