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