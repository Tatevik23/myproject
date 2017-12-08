#!/usr/bin/env bash
passfiles=pass_files
failfiles=fail_files
#Remove directories if they exists to be able to create new ones.
if [ -d $passfiles ] && [ -d $failfiles ]
then 
    rm -rf "$passfiles"
    rm -rf "$failfiles"
fi

mkdir $passfiles
mkdir $failfiles

# Find all files in log directory recursively.
allfiles=`find ./log/ -type f`

#Loop over all files, find all pass files and copy them in newly created 'passfiles' directory with $file_pass names. The same for fail files.
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

#Print pass & fail files count
echo "Pass files count" 
ls ./pass_files/ | wc -l
echo "Fail files count"
ls ./fail_files/ | wc -l
