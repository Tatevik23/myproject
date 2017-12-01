#!/usr/bin/evn bash
fileStrings=$(cat $1)
lines=($fileStrings)
lenght=${#lines[@]}
#Bubble sort 
for (( i=0; i < $lenght; i++))
do
    for (( j=$i; j < $lenght; j++))
    do 
        if [ ${lines[$i]} \> ${lines[$j]} ]; then
            tmp=${lines[$i]}
            lines[$i]=${lines[$j]}
            lines[$j]=$tmp
        fi
    done
done

if [ -f "outputResult" ]; then
   rm -rf "outputResult"
fi    

for j in ${lines[@]}
do
    echo $j >>outputResult
done 
