#!/bin/bash
nasm -f elf64 "$1"_temp.s
if test -f "$1"_temp.o; then
    ld -o "$1" "$1"_temp.o
    rm "$1"_temp.o
    rm "$1"_temp.s
    echo "Run:"
    echo ""
    ./"$2"
else 
    echo "Assembling ended with some errors."
fi