#!/usr/bin/env python3
import configparser
import sys
import os
import xml.etree.ElementTree as ET
config_file = sys.argv[1]
# Getting input files names as list from config.ini file
def configmap(fileName):
    config = configparser.ConfigParser()
    config.readfp(open(fileName))
    input_files = config['SectionOne']['input_files'].split()
    return input_files

# Getting input file from config.ini file to update min and max tag values
def getting_update_file(fileName):
    config = configparser.ConfigParser()
    config.readfp(open(fileName))
    in_out = config['SectionOne']['in_out_file']
    inout = []
    inout.append(in_out)
    return inout
#in_out_file = getting_update_file(config_file)
#print(in_out_file)

# Getting path from config.ini file for input files
def getting_path(configfilename):
    config = configparser.ConfigParser()
    config.readfp(open(configfilename))
    path = config['SectionOne']['file_paths']
    return path

# Merging input file and directory to getting input files
def merging_path_file():
    file_paths = configmap(config_file)
    directory = getting_path(config_file)
    files = []
    for filename in file_paths:
        myfile = os.path.join(directory, filename)
        files.append(myfile)
    return files


def getting_min_max(file_with_tags,tag, min_max_tag): 
#    input_files = merging_path_file(configmap(config_file))
    min_value = []
    for parse_file in file_with_tags:
        tree = ET.parse(parse_file)
        root = tree.getroot()
        for child in root.findall(tag):
            minValue = child.find(min_max_tag).text
            min_value.append(minValue)
    return min_value
   
def getting_min_value(input_files,in_out_file,min_tag_tree):
    tree = ET.parse('in_out.xml')
    root = tree.getroot()
    min_tag = root.find(min_tag_tree)
    minimum = min(input_files)
    print(minimum,63,in_out_file[0])
    if minimum < in_out_file[0]:
        min_tag.text = minimum
        print(min_tag.text)
        min_tag.set('updated','yes')
        tree.write('in_out.xml')
   # for x in input_files:
      #  if input_files[0] > x:
    #    if x < in_out_file[0]:
     #       min_tag.text = x
      #      min_tag.set('updated','yes')
       #     tree.write('in_out.xml')
           # return min_tag.text
       # else:
        #    return in_out_file[0]  
print(getting_min_max(merging_path_file(),'Tatev','min'))
print(getting_min_max(getting_update_file(config_file),'Tatev','min'))
#print(min(getting_min_max(merging_path_file(),'Tatev','min') + getting_min_max(getting_update_file(config_file),'Tatev','min'))

getting_min_value(getting_min_max(merging_path_file(),'Tatev','min'),getting_min_max(getting_update_file(config_file),'Tatev','min'),'./Tatev/min')
getting_min_value(getting_min_max(merging_path_file(),'Gayane','min'),getting_min_max(getting_update_file(config_file),'Gayane','min'),'./Gayane/min')

    
def getting_max_value(input_files,in_out_file,max_tag_tree):
#    values = getting_min_max(merging_path_file(),'Tatev', 'max')
#    var = getting_min_max(getting_update_file(config_file),'Tatev','max')
#    print(input_files)
 #   print(in_out_file)
    tree = ET.parse('in_out.xml')
    root = tree.getroot()
    max_tag = root.find(max_tag_tree)
    for var in input_files:
#        if input_files[0] < var:
        if var > in_out_file[0]:
            max_tag.text = var
            max_tag.set('updated','yes')
            tree.write('in_out.xml')
         #   return var
      #  else:
       #     return in_out_file[0]
    
#getting_max_value(getting_min_max(merging_path_file(),'Tatev','max'),getting_min_max(getting_update_file(config_file),'Tatev','max'),'./Tatev/max')
#getting_max_value(getting_min_max(merging_path_file(),'Gayane','max'),getting_min_max(getting_update_file(config_file),'Gayane','max'),'./Gayane/max')


#print(getting_max_value(getting_min_max(merging_path_file(),'Tatev','max'),getting_min_max(getting_update_file(config_file),'Tatev','max')))
#print(getting_min_value(getting_min_max(merging_path_file(),'Tatev','min'),getting_min_max(getting_update_file(config_file),'Tatev','min')))
#print(getting_min_max(merging_path_file(),'Tatev', 'min')) 
#print(getting_min_max(merging_path_file(),'Tatev','max')) 
#print(getting_min_max(merging_path_file(),'Gayane','min'))
#print(getting_min_value(getting_min_max(merging_path_file(),'Gayane','min'),getting_min_max(getting_update_file(config_file),'Gayane','min'))
var = getting_min_max(merging_path_file(),'Gayane','min')
var1 = getting_min_max(getting_update_file(config_file),'Gayane','min')
#print(getting_min_value(var,var1))
print(getting_min_max(merging_path_file(),'Gayane','min'))
print(getting_min_max(getting_update_file(config_file),'Gayane','min'))
#print(getting_min_max(getting_update_file(config_file),'Tatev', 'min'))

def newfunc():
    tree = ET.parse('in_out.xml')
    root = tree.getroot()
    min_tag = root.find('./Tatev/min')
    tatev_min = getting_min_value(getting_min_max(merging_path_file(),'Tatev','min'),getting_min_max(getting_update_file(config_file),'Tatev','min'))
    min_tag.text = tatev_min
    min_tag.set('updated', 'yes')
    max_tag = root.find('./Tatev/max')
    tatev_max = getting_max_value(getting_min_max(merging_path_file(),'Tatev','max'),getting_min_max(getting_update_file(config_file),'Tatev','max'))
    max_tag.text = tatev_max
    max_tag.set('updated','yes')
#    min_tag_gayane = root.find('./Gayane/min')
#    gayane_min = getting_min_value(getting_min_max(merging_path_file(),'Gayane','min'),getting_min_max(getting_update_file(config_file),'Gayane','min'))
#    min_tag_gayane.text = gayane_min
#    min_tag_gayane.set('updated','yes')
#    max_tag_gayane = root.find('./Gayane/max')
#    gayane_max = getting_max_value(getting_min_max(merging_path_file(),'Gayane','max'),getting_min_max(getting_update_file(config_file),'Gayane','max'))
#    max_tag_gayane.text = gayane_max
#    max_tag_gayane.set('updated','yes')
#    tree.write('in_out.xml')
#    print(tag.text,32)
#newfunc()
