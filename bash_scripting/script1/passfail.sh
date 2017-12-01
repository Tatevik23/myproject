#!/usr/bin/env bash
passfiles=pass_files
failfiles=fail_files
#Remove files
if [ -d $passfiles ] && [ -d $failfiles ]
then 
    rm -rf "$passfiles"
    rm -rf "$failfiles"
fi

mkdir $passfiles
mkdir $failfiles
#Loop for all files
allfiles=`find ./log/ -type f`
for file in $allfiles
do
    if [ -f $file ]
    then
        if grep -q -i 'pass' $file -R
        then
            cp $file $passfiles/$(basename $file)"_pass"
        else
            cp $file $failfiles/$(basename $file)"_fail"
        fi
    fi
done
#Pass & fail files count
echo "Pass files count" 
ls ./pass_files/ | wc -l
echo "Fail files count"
ls ./fail_files/ | wc -l
