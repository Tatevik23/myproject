#!/usr/bin/evn bash
fileStrings=$(cat $1)
echo $fileStrings 
lines=($fileStrings)
echo ${lines[2]}
#IFS=$'\n' read -d -r -a lines < $1
lenght=${#lines[@]}
echo $lenght
for (( i = 0; i < $lenght; i++))
do
    echo ${lines[$i]}
done

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

for (( i=0; i < $lenght; i++))
do 
    echo ${lines[$i]}
done
if [ -f "outputresult" ]; then
    rm -rf "outputResult"
fi    

for j in ${lines[@]}
do
    echo $j >>outputResult
done 
