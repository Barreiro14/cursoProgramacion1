#!/bin/bash

#Este script suma dos valores 

echo "Introduce el primer valor"

read a 

echo "Introduce el segundo valor" 

read b

echo "Introduce el tercer valor"

read c

echo "La suma total es:"

echo $((a + b + c))

#Lo hice con tres valores para variar

#agrego algunas notas para recordar

#El comando read interrumpe la ejecución del shell hasta que el usuario introduzca una cadena de caracteres (aunque sea vacía) en su entrada estándar.
#Las palabras que componen la cadena de caracteres escrita por el usuario se asignan a las variables cuyos nombres se pasan como argumentos al comando read.

#Expansion aritmetica $(( ))

