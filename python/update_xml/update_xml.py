#!/usr/bin/env python3
import configparser
import sys
import os
import xml.etree.ElementTree as ET
config_file = sys.argv[1]
def configmap(fileName):
    config = configparser.ConfigParser()
    config.readfp(open(fileName))
    input_files = config['SectionOne']['input_files'].split()
    return input_files

def getting_update_file(fileName):
    config = configparser.ConfigParser()
    config.readfp(open(fileName))
    in_out = config['SectionOne']['in_out_file']
    return in_out
in_out_file = getting_update_file(config_file)
print(in_out_file)

def getting_path(configfilename):
    config = configparser.ConfigParser()
    config.readfp(open(configfilename))
    path = config['SectionOne']['file_paths']
    return path

def merging_path_file():
    file_paths = configmap(config_file)
    directory = getting_path(config_file)
    files = []
    for filename in file_paths:
        myfile = os.path.join(directory, filename)
        files.append(myfile)
    return files

def getting_min_max(tag, min_max_tag): 
    input_files = merging_path_file()
    min_value = []
    for parse_file in input_files:
        tree = ET.parse(parse_file)
        root = tree.getroot()
        for child in root.findall(tag):
            minValue = child.find(min_max_tag).text
            min_value.append(minValue)
    return min_value
   
def getting_min_value():
    var = getting_min_max('Tatev','min')
    for x in var:
        if var[0] > x:
            return x

def getting_max_value():
    values = getting_min_max('Tatev', 'max')
    for x in values:
        if values[0] < x:
            return x

print(getting_max_value())
print(getting_min_value())
print(getting_min_max('Tatev', 'min')) 
print(getting_min_max('Tatev','max')) 
print(getting_min_max('Gayane','min'))
