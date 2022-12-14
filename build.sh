nasm -f elf64 -l "$1".lst "$1".s
ld -o "$1" "$1".o
rm "$1".o
rm "$1".lst
./"$1"