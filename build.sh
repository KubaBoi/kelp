nasm -f elf64 -l test.lst test.s
ld -o test test.o
rm test.o
rm test.lst
./test