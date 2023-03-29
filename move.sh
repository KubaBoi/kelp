#!/bin/bash

DIRECTORY="./examples/"
if test -f "$DIRECTORY$1.s"; then
    echo "File $DIRECTORY$1.s already exists."
    read -p "Do you want to continue? [y/n] " yn;
    case $yn in
        [Yy]* ) echo "OK";;
        * ) exit;;
    esac
fi

cp "./test.s" "$DIRECTORY$1.s";