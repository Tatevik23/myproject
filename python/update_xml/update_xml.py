#!/usr/bin/env python3
import configparser
import sys
import os
import xml.etree.ElementTree as ET
config_file = sys.argv[1]
  
def read_from_config(config, section):
    requested_section = config["SectionOne"][section]
    return requested_section

# Parsing all input xml files and in_out.xml file to find minimum and maximum values which are inside <min> and <max> tags respectively and update in_out file.
def parse_xml(inout_file,input_files):
    tree = ET.parse(inout_file)
    root = tree.getroot()
    for inputs in input_files:
        inputs_tree = ET.parse(inputs)
        inputs_root = inputs_tree.getroot()
        for child in inputs_root:
            for var in root:
                if child.tag == var.tag:
                    print(87,child.tag,inputs)
                    print(child.find("min").text,var.find("min").text,"min")
                    child_min = int(child.find("min").text)
                    var_min = int(var.find("min").text)
                    min_value = min(child_min, var_min)
                    var.find("min").text = str(min_value)
                    print(child.find("max").text,var.find("max").text,"max")
                    child_max = int(child.find("max").text)
                    var_max = int(var.find("max").text)
                    max_value = max(child_max, var_max)
                    var.find("max").text = str(max_value)
                    tree.write(inout_file)
                    print(min_value,max_value) 

def main():
    config = configparser.ConfigParser()
    config.readfp(open(config_file))
    inout_file = read_from_config(config, "in_out_file")
    files_path = read_from_config(config, "files_path")
    input_files = []
    for filename in os.listdir(files_path):
        input_files.append(os.path.join(files_path,filename))
    print(input_files,inout_file)
    parse_xml(inout_file,input_files)
main()
