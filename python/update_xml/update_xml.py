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
file_paths = configmap(config_file)
def getting_path(configfilename):
    config = configparser.ConfigParser()
    config.readfp(open(configfilename))
    path = config['SectionOne']['file_paths']
    return path
directory = getting_path(config_file)
for filename in file_paths:
    print(os.path.join(directory, filename)) 
    myfile = os.path.join(directory, filename)  
    tree = ET.parse(myfile)
    root = tree.getroot()
        
    print(root.tag) 
