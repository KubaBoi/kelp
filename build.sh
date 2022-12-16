nasm -f elf64 "$1".s
if test -f "$1.o"; then
    ld -o "$1" "$1".o
    rm "$1".o
    ./"$1"
fi