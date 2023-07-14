#!/bin/bash

touch data.dat

pepe=1
while [ $pepe -le 100 ]
do
  echo "$pepe"
  pepe=$(( $pepe + 1 ))
done > "data.dat" 

