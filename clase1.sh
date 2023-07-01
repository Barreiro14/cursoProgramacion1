#!/bin/bash

m="$1"

str1="iq"
str2="rank"
str3="country"
str4="pop2022"

test(){
    sum=0
    touch elprofeejevi.txt
    #echo "$m"
    tr -d '"' < iqporpaises.csv > iqporpaises2.csv
    while IFS=, read rank country iq pop2022; do
        if [[ "$m" = "$str1" ]]; then
            echo "$iq" >> elprofeejevi.txt
        elif [[ "$m" = "$str2" ]]; then
            echo "$rank" >> elprofeejevi.txt
        elif [[ "$m" = "$str3" ]]; then
            echo "$country" >> elprofeejevi.txt
        else [[ "$m" = "$str4" ]]; 
            echo "$pop2022" >> elprofeejevi.txt
        fi
    done < "iqporpaises2.csv" 
    #echo "test"
}

test