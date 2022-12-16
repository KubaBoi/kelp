; STRING instructions
;           Operands        Desctription        Byte Op.    Word Op.    DWord Op.
; MODS      ES:DI, DS:SI       This instruction MOVSB       MOVSW       MOVSD
;                           moves 1 Byte, Word 
;                           or Doubleword of
;                           data from memory
;                           location to another.
; LODS      AX, DS:SI          This instruction LODSB       LODSW       LODSD
;                           loads from memory.
;                           If the operand is
;                           of one byte, it is 
;                           loaded into the AL 
;                           register, if the 
;                           operand is one word, 
;                           it is loaded into 
;                           the AX register and 
;                           a doubleword is 
;                           loaded into the EAX 
;                           register.
; STOS      ES:DI, AX          This instruction STOSB       STOSW       STOSD
;                           stores data from 
;                           register 
;                           (AL, AX, or EAX) 
;                           to memory.
; CMPS      DS:SI, ES:DI       This instruction CMPSB       CMPSW       CMPSD
;                           compares two data 
;                           items in memory. 
;                           Data could be of 
;                           a byte size, word 
;                           or doubleword.
; SCAS      ES:DI, AX          This instruction SCASB       SCASW       SCASD
;                           compares the 
;                           contents of 
;                           a register 
;                           (AL, AX or EAX) 
;                           with the contents 
;                           of an item 
;                           in memory.

; REP           repeats instruction until CX is not zero
; REPE/REPZ     repeats while ZF is zero. Stops when ZF or CX is zero
; REPNE/REPNZ   repeats while ZF is not zero. Stops when ZF ZF is zero or CX is decremented to zero
