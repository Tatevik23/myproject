#!/usr/bin/python3
import sys, re
# Find words by regular expression  and write into new file
def regExpFunction(search_file):
    content = open(search_file).read()
    match_words = re.findall(r'(?<!\.\s)\b[A-Z][a-z]*\b', content)
    print(match_words)
    output_file = open("output_file.txt", 'w')
    for word in match_words:
        output_file.write(word + ' ')
   
def mainFunc():
    input_file = sys.argv[1]
    regExpFunction(input_file)
mainFunc()
