# kelp

## syscals

/usr/include/asm-generic/unistd.h

# Registers

- General registers
    - Data registers
    - Pointer registers
    - Index registers
- Control registers
- Segment registers

## Data registers

| Code | Name | Description |
| --- | --- | --- |
| EAX | Accumulator | It is used in input/output and most arithmetic instructions. For example, in multiplication operation, one operand is stored in EAX or AX or AL register according to the size of the operand. |
| EBX | Base | It could be used in indexed addressing. |
| ECX | Counter | Store the loop count in iterative operations. |
| EDX | Data | It is also used in input/output operations. It is also used with AX register along with DX for multiply and divide operations involving large values. |

## Pointer registers

The pointer registers are 32-bit EIP, ESP, and EBP registers and corresponding 16-bit right portions IP, SP, and BP.

| Code | Name | Description |
| --- | --- | --- |
| EIP | Instruction pointer | The 16-bit IP register stores the offset address of the next instruction to be executed. IP in association with the CS register (as CS:IP) gives the complete address of the current instruction in the code segment.
| ESP | Stack pointer | The 16-bit SP register provides the offset value within the program stack. SP in association with the SS register (SS:SP) refers to be current position of data or address within the program stack.
| EBP | Base pointer | The 16-bit BP register mainly helps in referencing the parameter variables passed to a subroutine. The address in SS register is combined with the offset in BP to get the location of the parameter. BP can also be combined with DI and SI as base register for special addressing.

## Index registers

The 32-bit index registers, ESI and EDI, and their 16-bit rightmost portions. SI and DI, are used for indexed addressing and sometimes used in addition and subtraction. 

| Code | Name | Description |
| --- | --- | --- |
| ESI | Source index | It is used as source index for string operations.
| EDI | Destination index | It is used as destination index for string operations.

## Control register

The 32-bit instruction pointer register and the 32-bit flags register combined are considered as the control registers.

Many instructions involve comparisons and mathematical calculations and change the status of the flags and some other conditional instructions test the value of these status flags to take the control flow to other location.

| Code | Name | Description |
| --- | --- | --- |
| OF | Overflow flag | It indicates the overflow of a high-order bit (leftmost bit) of data after a signed arithmetic operation.
| DF | Direction flag | It determines left or right direction for moving or comparing string data. When the DF value is 0, the string operation takes left-to-right direction and when the value is set to 1, the string operation takes right-to-left direction.
| IF | Interrupt flag | It determines whether the external interrupts like keyboard entry, etc., are to be ignored or processed. It disables the external interrupt when the value is 0 and enables interrupts when set to 1.
| TF | Trap flag | It allows setting the operation of the processor in single-step mode. The DEBUG program we used sets the trap flag, so we could step through the execution one instruction at a time.
| SF | Sign flag | It shows the sign of the result of an arithmetic operation. This flag is set according to the sign of a data item following the arithmetic operation. The sign is indicated by the high-order of leftmost bit. A positive result clears the value of SF to 0 and negative result sets it to 1. 
| ZF | Zero flag | It indicates the result of an arithmetic or comparison operation. A nonzero result clears the zero flag to 0, and a zero result sets it to 1.
| AF | Auxiliary carry flag | It contains the carry from bit 3 to bit 4 following an arithmetic operation; used for specialized arithmetic. The AF is set when a 1-byte arithmetic operation causes a carry from bit 3 into bit 4. 
| PF | Parity flag | It indicates the total number of 1-bits in the result obtained from an arithmetic operation. An even number of 1-bits clears the parity flag to 0 and an odd number of 1-bits sets the parity flag to 1.
| CF | Carry flag | t contains the carry of 0 or 1 from a high-order bit (leftmost) after an arithmetic operation. It also stores the contents of last bit of a shift or rotate operation.