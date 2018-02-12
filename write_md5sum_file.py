#!/usr/bin/env python

## Scripts is based on PythonConfluenceAPI package.
## It takes all Confluence pages(all content ids) and checks if exists
## file there or not. If file does not exist script creates it, in 
## other case updates it
##
## Requirements:
##  Please install PythonConfluenceAPI and future packages
##  For install use pip comand like this
##
##   pip install PythonConfluenceAPI
##   pip install future
## 
## For running script:
##  ./write_md5sum_file.py username password file_path file page_id 

try:
    import sys
    import os
    import urllib
    import json
    from PythonConfluenceAPI import ConfluenceAPI
except ImportError as exception: 
    print "%s - Please install the necessary libraries." % exception
    sys.exit()

# Getting comand line arguments
user = sys.argv[1]
pswd = sys.argv[2]
source_path = sys.argv[3]
file_name = sys.argv[4]

# If page id is not inserted, default is 3047893
try:
    page_id = sys.argv[5]
except:
    page_id = "3047893"

url = "http://confluence.marketcomllc.com/rest/api/content/"
api = ConfluenceAPI(user, pswd, 'http://confluence.marketcomllc.com/')

# For testing
#url = "http://dev.confluence.marketcomllc.com:8090/rest/api/content/"
#api = ConfluenceAPI(user, pswd, 'http://dev.confluence.marketcomllc.com:8090/')

def get_content_dict(url):
    """Getting content with all page ids
    Args:
        url - Confluence url
    Return:
        page content as a dictionary
    """
    open_url = urllib.urlopen(url)
    content = open_url.read()
    return json.loads(content)


# Write/update file into Confluence known page with given page id 
file_object = open(os.path.join(source_path, file_name), 'r')
attachment = {"file": file_object, "comment": ""}
attachment_url = url + page_id + "/child/attachment?filename=" + file_name    
attachment_content = get_content_dict(attachment_url)
if not attachment_content.has_key("results"):
    print "%s - Invalid page id" % page_id
    sys.exit()
elif attachment_content["results"]: 
    api.update_attachment(page_id, attachment_content["results"][0]["id"], attachment, callback=None)
    print "%s file successfully updated." % file_name
else:
    api.create_new_attachment_by_content_id(page_id, attachment, callback=None)
    print "%s file successfully writed." % file_name
file_object.close()
