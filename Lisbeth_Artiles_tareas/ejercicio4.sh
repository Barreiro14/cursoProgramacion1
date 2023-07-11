#!/bin/bash

archivo="datos.dat"


if [ -f "$archivo" ]; then
    
    while IFS= read -r linea; do
        echo "$linea"
    done < "$archivo"
else
    echo "El archivo $archivo no existe."
    exit 1
fi
