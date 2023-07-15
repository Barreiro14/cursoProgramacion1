#!/bin/bash

touch data.dat

n=1

while [ $n -le 100 ]
do
  echo $n  $(($n + 1))  $(($n + 2))  $(($n+3))  $(($n+4)) >> data.dat
  n=$(( $n + 5 ))
done
