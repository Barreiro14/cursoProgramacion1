#!/bin/bash

file="$1"

arg="$2"

str1="arg1"
str2="arg2"
str3="arg3"
str4="arg4"

test(){
    sum=0
    touch archivo2.txt
    tr -d '"' < "$file" > output.csv
    while IFS=, read arg1 arg2 arg3 arg4; do
        if [[ "$arg" = "$str1" ]]; then
            echo "$arg1" >> archivo2.txt
        elif [[ "$arg" = "$str2" ]]; then
            echo "$arg2" >> archivo2.txt
        elif [[ "$arg" = "$str3" ]]; then
            echo "$arg3" >> archivo2.txt
        else [[ "$arg" = "$str4" ]]; 
            echo "$arg4" >> archivo2.txt
        fi
    done < "output.csv" 
    echo "Valor asignado al ($arg):"
    cat archivo2.txt
    echo "Primera linea:"
    head -n 1 archivo2.txt
}

test
