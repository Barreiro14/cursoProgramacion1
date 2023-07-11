#!/bin/bash

carpeta="impresora"
cd "$carpeta" || exit 1

programa="./imprimir.sh"

if [ -x "$programa" ]; then 
    "./$programa"
else 
echo "El programa no existe."
exit 1
fi