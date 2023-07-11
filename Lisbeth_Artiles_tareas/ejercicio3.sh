#!/bin/bash

archivo="datos.dat"
exec 3> "$archivo"

for ((i=1; i<=100; i++)); do 
     echo "$i" >&3
done

cat "$archivo"
exec 3>&-
