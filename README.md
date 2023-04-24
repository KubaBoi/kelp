# Kelp

First two bytes are count of needed variables inside program. Those two bytes describes how many addresses would be needed and at the start of the program there would be created an array with values of addresses in memory.

This array (`mem_map`) will be filled with 0s for signalization that addresses are not allocated yet and those addresses will be as `nullptr`.

## Addreses

Addreses are 2 bytes integers of 256-decimal number system (as every number in this system) as little endian.

- `1` = 1 0
- `6` = 6 0
- `258` = 2 1

## TODO

- `SUM`, `SUB`, `MUL` and `DIV` byte range
- memory fractions + `FRE`

## Instructions

| Name | Code | Arg count | Description | arg0 | arg1 | arg2 | arg3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `KILL` | 0 | 0 | End process - should be at the end of source | 
| `OUT` | 1 | 3 | Print `n` count of bytes from `addr` as `type` | `type`: `0`-str, `1`-char, `2`-dec, `3`-n_bytes | `n`: count of bytes to be printed (no matter if `type`=0,1. In `type`=2 case that means how many bytes should be converted into decimal.) | `addr`: addr |
| `SET` | 2 | 2... | Set `n` bytes at `addr`. | `addr`: symbolic address in memory map. | `n` | There would be `n` args/bytes which would be saved into memory. | 
| `SUM` | 3 | 3 | Sum `a` with `b` and save result into `dest` | `dest`: addr | `a`: addr | `b`: addr |
| `SUB` | 4 | 3 | Substract `b` from `a` and save result into `dest` | `dest`: addr | `a`: addr | `b`: addr |
| `MUL` | 5 | 3 | Multiply `a` by `b` and save result into `dest` | `dest`: addr | `a`: addr | `b`: addr |
| `DIV` | 6 | 4 | Divide `a` by `b` and save result into `dest` and modulo into `mod` | `dest`: addr | `mod`: addr | `a`: addr | `b`: addr |
| `CPY` | 7 | 3 | Copy `n` first bytes of `targ` into `dest` | `n`: count of bytes | `dest`: addr | `targ`: addr | 
| `ALC` | 8 | 2 | Allocate `n` count of bytes in memory at `addr`. | `addr`: addr | `n`: count of bytes (2byte) |
| `FRE` | 9 | 0 | Not implemented |
| `OFL` | 10 | 3 | Open file at `addr` with `mode` and return `ptr` to opened file. | `ptr`: addr (4bytes space) | `addr`: addr of memory  with string path | `mode`: `0`-r, `1`-w, `2`-a, `3`-w+ |
| `CFL` | 11 | 1 | Close file with `ptr` | `ptr`: addr |

## Examples

HelloWorld:

```c
1, 0, // count of variables in programm
8, 0, 0, 13, 0, // allocate 13 bytes in mem at addr 0 0
// SET next 13 bytes into memory at address 0 0
2, 0, 0, 13, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!', 0,
1, 0, 0, 0, 0, // OUT str at address 0 0
0 // end
```

Sum:
```c
3, 0, // count of variables in programm
// allocate 1 byte for addresses 0 0 - 2 0
8, 0, 0, 1, 0,
8, 1, 0, 1, 0,
8, 2, 0, 1, 0,
// SET 1 byte of value 5 at address 0 0
2, 0, 0, 1, 5,
// SET 1 byte of value 10 at address 1 0
2, 1, 0, 1, 10,
// SET 1 byte at 0 address 2 0
2, 2, 0, 1, 0,
// SUM 0 0 + 1 0 and save result in 2 0
3, 2, 0, 0, 0, 1, 0,
// OUT dec as 1 byte at address 2 0
1, 2, 1, 2, 0,
0
```