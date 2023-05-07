# Kelp Virtual Machine

First two bytes are count of needed variables inside program. Those two bytes describes how many addresses would be needed and at the start of the program there would be created an array with values of addresses in memory.

This array will be filled with 0s for signalization that addresses are not allocated yet and those addresses will be considered as `nullptr`.

Next 4 bytes are `CALL` instruction to call `main` method of program and to `KILL` instruction after `main` return. 

`main` is not called with arguments, because those arguments are in static address `0 0` and VM will fills them.

## Addreses

Addreses are 2 bytes integers of 256-decimal number system (as every number in this system) as little endian.

- `1` = 1 0
- `6` = 6 0
- `258` = 2 1

## Pointers

There is an array of pointers `mem` where every item has only one relation item in `memory`. But items in `memory` could have more relation items from `mem`.

- `mem` is a array of indexes for `memory`.
- `memory` is an actual memory of program, but this array if only abstract.

## Math operations

All math operations (`SUM`, `SUB`, `MUL` and `DIV`) are able to operate with different data types (4 bytes + 2 bytes = 4 bytes), but result memory need to respect the size of the result. It means that if the result would be size of 4 bytes and result memory would be allocated for less than 4 bytes (for example 2 bytes) then some information will be probably lost. Because saved would be only first (for example) 2 bytes of the result. 

## Condition type

Condition type is one byte, first 1 bit is direction and the other 7 bits are type of condition:

| Code | Bits | Name | Description |
| --- | --- | --- | --- |
| 0 | 0000000 0 | `FEQ` | forwards if equal `==` |
| 1 | 0000000 1 | `BEQ` | backwards if equal `==` |
| 2 | 0000001 0 | `FNQ` | forwards if NOT equal `!=` |
| 3 | 0000001 1 | `BNQ` | backwards if NOT equal `!=` |
| 4 | 0000010 0 | `FGE` | forwards if equal `>=` |
| 5 | 0000010 1 | `BGE` | backwards if equal `>=` |
| 6 | 0000011 0 | `FLE` | forwards if equal `<=` |
| 7 | 0000011 1 | `BLE` | backwards if equal `<=` |
| 8 | 0000100 0 | `FG` | forwards if equal `>` |
| 9 | 0000100 1 | `BG` | backwards if equal `>` |
| 10 | 0000101 0 | `FL` | forwards if equal `<` |
| 11 | 0000101 1 | `BL` | backwards if equal `<` |

## Instructions

| Name | Code | Arg count | Description | arg0 | arg1 | arg2 | arg3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `KILL` | 0 | 0 | End process - should be at the end of source | 
| `OUT` | 1 | 2 | Print bytes from `addr` as `type` | `type`: `0`-str, `1`-char, `2`-dec | `addr`: addr |
| `SET` | 2 | 3... | Set `n` bytes at `addr` with `offset`. | `addr`: symbolic address in memory map. | `offset`: (2bytes) | `n`: (2bytes) | There would be `n` args/bytes which would be saved into memory. | 
| `CPT` | 3 | 2 | Copy address of `targ` to `dest` | `dest`: addr | `targ`: addr | 
| `CPY` | 4 | 3 | Copy `n` first bytes of `targ` into `dest` | `n`: count of bytes (2bytes) | `dest`: addr | `targ`: addr | 
| `ALC` | 5 | 2 | Allocate `n` count of bytes in memory at `addr`. | `addr`: addr | `n`: count of bytes (2bytes) |
| `FRE` | 6 | 1 | Free memory at `addr` | `addr`: addr |
| `RLC` | 7 | 2 | Realloc memory ar `addr` by `n` bytes | `addr`: addr | `n`: new bytes size (2bytes) |
| `SUM` | 8 | 3 | Sum `a` with `b` and save result into `dest` | `dest`: addr | `a`: addr | `b`: addr |
| `SUB` | 9 | 3 | Substract `b` from `a` and save result into `dest` | `dest`: addr | `a`: addr | `b`: addr |
| `MUL` | 10 | 3 | Multiply `a` by `b` and save result into `dest` | `dest`: addr | `a`: addr | `b`: addr |
| `DIV` | 11 | 4 | Divide `a` by `b` and save result into `dest` and modulo into `mod` | `dest`: addr | `mod`: addr | `a`: addr | `b`: addr |
| `CALL` | 12 | 1... | Call method at `addr` with `args` and return back from where method was called. | `addr`: addr | `args`: addresses of arguments of method |
| `RET` | 13 | 1 | Return from method back where it was called |
| `JMP` | 14 | 2 | Jump `n` bytes in `direction` in source code. | `direction`: 0-forwards, 1-backwards | `n`: count of bytes (2bytes) | 
| `JMC` | 15 | 4 | Jump `n` bytes in `direction` in source code if `agr0` with `arg1` fullfill `condition` | `condition`: first 1. bit is `direction`(0-forwards, 1-backwards), other bits are `condition type` | `n`: count of bytes (2bytes) | `arg0`: addr | `arg1`: addr |

## Examples

DEPRACATED

HelloWorld:

```c
1, 0, // count of variables in program
8, 0, 0, 13, 0, // allocate 13 bytes in mem at addr 0 0
// SET next 13 bytes into memory at address 0 0
2, 0, 0, 0, 0, 13, 0, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', 0,
1, 0, 0, 0, 0, // OUT str at address 0 0
0 // end
```

Sum:
```c
3, 0, // count of variables in program
// allocate 1 byte for addresses 0 0 - 2 0
8, 0, 0, 1, 0,
8, 1, 0, 1, 0,
8, 2, 0, 1, 0,
// SET 1 byte of value 5 at address 0 0
2, 0, 0, 0, 0, 1, 0, 5,
// SET 1 byte of value 10 at address 1 0
2, 1, 0, 0, 0, 1, 0, 10,
// SET 1 byte at 0 address 2 0
2, 2, 0, 0, 0, 1, 0, 0,
// SUM 0 0 + 1 0 and save result in 2 0
3, 2, 0, 0, 0, 1, 0,
// OUT dec as 1 byte at address 2 0
1, 2, 1, 2, 0,
0
```