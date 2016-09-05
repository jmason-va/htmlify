import os
import textwrap
from collections import OrderedDict
# TODO: test adding this to html tags
# <meta http-equiv="refresh" content="3" >


def read_file(file_name):
    """ opens a text file and returns its content as a list of strings"""
    infile = open(file_name, 'r')
    file_content = []   
    for line in infile.readlines():
        line = line.rstrip('\n')                
        file_content.append(line)   
    infile.close()
    return file_content


def print_file(file_name):
    """ prints file """
    infile = open(file_name, 'r')  
    for line in infile.readlines():
        print line
    infile.close()

def write_file_to_html(file_name, path_to_file, content):
    """ takes content and a filename, opens the file and writes the content to it """
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)
    outfile = open(path_to_file + file_name, 'w')

    for line in content:
        outfile.write(line + '<br>')
    outfile.close()


def convert_file_type(file_name, filetype):
    """returns a string with a different file type"""
    file_name = file_name.split('.')
    return '.'.join(file_name[:-1]) + '.' + filetype

def replace_in_str(content, dict_of_replace_tuples):
    """ 
    takes a list of content, and a dictionary, go through each line
    and replace each key in the dictionary with its value
    """
    content_str = '@#$%^&*('.join(content)               
    for item in OrderedDict(dict_of_replace_tuples):      
        content_str = content_str.replace(item, dict_of_replace_tuples[item]) 
    return_content = content_str.split('@#$%^&*(')               
    return return_content


def convert_tabs_and_newlines_in_html(content):
    """preserves line spacing when converting to a html file"""
    content = replace_in_str(content, {'\t': '&nbsp;&nbsp;&nbsp;&nbsp;', '\n': '<br>'})
    return content


def add_html_tags_and_stylesheet(content, stylesheet):
    """takes in content and a stylesheet name adds html tags and a stylesheet tag to the content"""
    convert_tabs_and_newlines_in_html(content)
    content.insert(0, "<html>\n<head><link rel='stylesheet' href='"+stylesheet+"'>\n<meta http-equiv='refresh' content='30' >\n</head>\n<body>\n<div class='container'>\n")
    content.append("\n</div>\n<div class='bg'></div>\n</body>\n</html>")
    return content


def process_file(infile, replacements, book_directory, publish_directory, stylesheet=None):
    """take a file in, change whatever you want in it, output it as html"""
    outfile = convert_file_type(infile, 'html')                 # create a html file with the same name
    content = read_file(book_directory + infile)                # read the file content and put it into content
    content = replace_in_str(content, replacements)             # go through and make replacements
    content = add_html_tags_and_stylesheet(content, stylesheet) # add html tags to content 
    write_file_to_html(outfile, publish_directory, content)     # write the file to the published folder

