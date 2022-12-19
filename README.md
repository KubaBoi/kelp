# kelp

## syscals

/usr/include/asm-generic/unistd.h

# Contents

- [Registers](#registers)
- [System calls](#system-calls)
- [Addressing](#addressing) 
- [Allocation](#allocation)
- [Constants](#constants)
- [Arithmetic instructions](#arithmetic-instruction)

# Registers

- General registers
    - [Data registers](#data-registers)
    - [Pointer registers](#pointer-registers)
    - [Index registers](#index-registers)
- [Control registers](#control-register)
- [Segment registers](#segment-registers)

## Data registers

| Code | Name | Description |
| --- | --- | --- |
| EAX | Accumulator | It is used in input/output and most arithmetic instructions. For example, in multiplication operation, one operand is stored in `EAX` or `AX` or `AL` register according to the size of the operand. |
| EBX | Base | It could be used in indexed addressing. |
| ECX | Counter | Store the loop count in iterative operations. |
| EDX | Data | It is also used in input/output operations. It is also used with `AX` register along with `DX` for multiply and divide operations involving large values. |

## Pointer registers

The pointer registers are 32-bit `EIP`, `ESP`, and `EBP` registers and corresponding 16-bit right portions `IP`, `SP`, and `BP`.

| Code | Name | Description |
| --- | --- | --- |
| EIP | Instruction pointer | The 16-bit `IP` register stores the offset address of the next instruction to be executed. `IP` in association with the `CS` register (as `CS:IP`) gives the complete address of the current instruction in the code segment.
| ESP | Stack pointer | The 16-bit `SP` register provides the offset value within the program stack. `SP` in association with the `SS` register (`SS:SP`) refers to be current position of data or address within the program stack.
| EBP | Base pointer | The 16-bit `BP` register mainly helps in referencing the parameter variables passed to a subroutine. The address in `SS` register is combined with the offset in `BP` to get the location of the parameter. `BP` can also be combined with DI and SI as base register for special addressing.

## Index registers

The 32-bit index registers, `ESI` and `EDI`, and their 16-bit rightmost portions. `SI` and `DI`, are used for indexed addressing and sometimes used in addition and subtraction. 

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
| CF | Carry flag | It contains the carry of 0 or 1 from a high-order bit (leftmost) after an arithmetic operation. It also stores the contents of last bit of a shift or rotate operation.

## Segment registers

Segments are specific areas defined in a program for containing data, code and stack.

Segments are specific areas defined in a program for containing data, code and stack. There are three main segments −

| Name | Description |
| --- | --- |
| Code Segment | It contains all the instructions to be executed. A 16-bit Code Segment register or `CS` register stores the starting address of the code segment.
| Data Segment | It contains data, constants and work areas. A 16-bit Data Segment register or `DS` register stores the starting address of the data segment.
| Stack Segment | It contains data and return addresses of procedures or subroutines. It is implemented as a 'stack' data structure. The Stack Segment register or SS register stores the starting address of the stack.

Apart from the `DS`, `CS` and `SS` registers, there are other extra segment registers - `ES` (extra segment), `FS` and `GS`, which provide additional segments for storing data.

In assembly programming, a program needs to access the memory locations. All memory locations within a segment are relative to the starting address of the segment. A segment begins in an address evenly divisible by 16 or hexadecimal 10. So, the rightmost hex digit in all such memory addresses is 0, which is not generally stored in the segment registers.

The segment registers stores the starting addresses of a segment. To get the exact location of data or instruction within a segment, an offset value (or displacement) is required. To reference any memory location in a segment, the processor combines the segment address in the segment register with the offset value of the location.

# System calls

There are six registers that store the arguments of the system call used: `EBX`, `ECX`, `EDX`, `ESI`, `EDI` and `EBP`. Arguments are consecutive and starting by with the `EBX`. If there are more than six arguments, then the memory location of the first argument is stored in the EBX.

| %eax | Name | %ebx | %ecx | %edx | %esx | %edi |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | sys_exit | int | - | - | - | - |
| 2 | sys_fork | struct pt_regs | - | - | - | - |
| 3 | sys_read | unsigned int | char * | size_t | - | - |
| 4 | sys_write | unsigned int | const char * | size_t | - | - |
| 5 | sys_open | const char * | int | int | - | - |
| 6 | sys_close | unsigned int | - | - | - | - |

# Addressing

- Register addressing
- Immediate addressing
- Memory addressing

## Register addressing

Register contains the operand:

```
MOV DX, TAX_RATE   ; Register in first operand
MOV COUNT, CX	   ; Register in second operand
MOV EAX, EBX	   ; Both the operands are in registers
```

Faster because data are stored in registers.

## Direct memory addressing

Data from memory. To locate the exact location of data in memory, we need the segment start address, which is typically found in the DS register and an offset value. The offset value is also called `effective address`.

The offset value specified by the variable name (pointer). The assembler calculates the offset value and maintains a symbol table, which stores the offset values of all the variables.

```
ADD	BYTE_VALUE, DL	; Adds the register in the memory location
MOV	BX, WORD_VALUE	; Operand from the memory is added to register
```

## Direct-Offset addressing

```
MOV CL, BYTE_TABLE[2]	; Gets the 3rd element of the BYTE_TABLE
MOV CL, BYTE_TABLE + 2	; Gets the 3rd element of the BYTE_TABLE
MOV CX, WORD_TABLE[3]	; Gets the 4th element of the WORD_TABLE
MOV CX, WORD_TABLE + 3	; Gets the 4th element of the WORD_TABLE
```

## Indirect Memory addressing

Used for variables containing several elements like arrays. Starting address of the array is stored in register.

```
MY_TABLE TIMES 10 DW 0  ; Allocates 10 words (2 bytes) each initialized to 0
MOV EBX, [MY_TABLE]     ; Value of MY_TABLE[0] in EBX -> EBX = 0
MOV EBX, MY_TABLE     ; Effective Address of MY_TABLE in EBX -> EBX = address
MOV [EBX], 110          ; MY_TABLE[0] = 110
ADD EBX, 2              ; EBX = EBX +2 , 2 because dw is 2 bytes
MOV [EBX], 123          ; MY_TABLE[1] = 123
```

# Allocation

`[variable_name] define_directive initial_value [,initial_value]...`

| Directive | Purpose | Storage Space |
| --- | --- | --- |
| DB | Define Byte | 1 byte |
| DW | Define Word | 2 bytes |
| DD | Define Doubleword | 4 bytes |
| DQ | Define Quadword | 8 bytes |
| DT | Define Ten Bytes | 10 bytes |

- Each byte of character is stored as its ASCII value in hexadecimal.
- Each decimal value is automatically converted to its 16-bit binary equivalent and stored as a hexadecimal number.
- Processor uses the little-endian byte ordering.
- Negative numbers are converted to its 2's complement representation.
- Short and long floating-point numbers are represented using 32 or 64 bits, respectively.

## Allocation for uninitialized data

| Directive | Purpose | Storage Space |
| --- | --- | --- |
| RESB | Reserve a Byte | 1 byte |
| RESW | Reserve a Word | 2 bytes |
| RESD | Reserve a Doubleword | 4 bytes |
| RESQ | Reserve a Quadword | 8 bytes |
| REST | Reserve a Ten Bytes | 10 bytes |

# Constants

- EQU
- %assign
    - allows redefinition
- %define
    - works like #define in C

# Arithmetic instruction

| Instruction | Syntax | Description |
| --- | --- | --- | 
| INC | INC destination | Increase operand by one |
| DEC | DEC destination | Decrease operand by one |
| ADD | ADD destination source | Add source operand to destination operand |
| SUB | SUB destination source | Substruct source operanf from destination operand |
| MUL | MUL multiplier | Multiplicant will be in `RAX` and result in `RAX` !! `RDX` will be set to zero |
| IMUL | IMUL multiplier | Used for signed |
| DIV | DIV divisor | Divide `RAX` by divisor -> result (quotient) RAX, (reminder) `RDX` !! `RDX` need to be 0|
| IDIV | IDIV divisor | Used for signed |

## MUL/IMUL

### When two bytes are multiplied

The multiplicand is in the `AL` register, and the multiplier is a byte in the memory or in another register. The product is in AX. High-order 8 bits of the product is stored in AH and the low-order 8 bits are stored in `AL`.

```
AL * 8 Bit Source = AH AL (AX)
```

### When two one-word values are multiplied

The multiplicand should be in the `AX` register, and the multiplier is a word in memory or another register. For example, for an instruction like `MUL DX`, you must store the multiplier in DX and the multiplicand in `AX`.

The resultant product is a doubleword, which will need two registers. The high-order (leftmost) portion gets stored in DX and the lower-order (rightmost) portion gets stored in `AX`.

```
AX * 16 Bit Source = DX DA
```

### When two doubleword values are multiplied

When two doubleword values are multiplied, the multiplicand should be in `EAX` and the multiplier is a doubleword value stored in memory or in another register. The product generated is stored in the `EDX:EAX` registers, i.e., the high order 32 bits gets stored in the `EDX` register and the low order 32-bits are stored in the `EAX` register.
