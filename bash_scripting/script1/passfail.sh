#!/usr/bin/env bash
passfiles=pass_files
failfiles=fail_files
if [ -d $passfiles ] && [ -d $failfiles ]
then 
    echo "MTAAV"
    rm -rf "$passfiles"
    rm -rf "$failfiles"
fi
allfiles=`find ./log/ -type f`
echo $allfiles
mkdir $passfiles
mkdir $failfiles

for file in $allfiles
do
    if [ -f $file ]
    then
        if grep -q -i 'pass' $file -R
        then
            cp $file $passfiles/$(basename $file)"_pass"
            echo $file
        else
            cp $file $failfiles/$(basename $file)"_fail"
        fi
    fi
done

echo "Pass files count" 
ls ./pass_files/ | wc -l
echo "Fail files count"
ls ./fail_files/ | wc -l
