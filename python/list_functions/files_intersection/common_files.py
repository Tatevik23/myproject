#!/usr/bin/python3
import sys
def getListFromFile(input_file):
    content = open(input_file, 'r').read().split()
    return content

# Find intersection between two lists and write it into new file.
def findIntersection(content1, content2):
    common = set(content1).intersection(content2)
    common = [' ' + x + ' ' for x in common]
    with open('output_file.txt', 'w') as file_out:
        for line in common:
            file_out.write(line)

def mainFunc():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    list1 = getListFromFile(file1)
    list2 = getListFromFile(file2)
    findIntersection(list1, list2)
mainFunc()  
