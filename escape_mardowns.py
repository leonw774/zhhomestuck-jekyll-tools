import os
import io
import re
path = "./_posts/"
for filenum, filename in enumerate(os.listdir(path)) :
    if filenum % 1000 == 0 : print(filenum)
    file_lines = open(path + filename, "r", encoding = 'utf-8').readlines()
    yml_string = "".join(file_lines[:10])
    story_string = "".join(file_lines[10:])
    story_string = story_string.replace("*", "&#42;")
    story_string = story_string.replace("/&#42;", "/*") #css comments
    story_string = story_string.replace("|", "&#124;")
    
    io.open(path + filename, 'w', encoding = 'utf-8', newline='\n').write(yml_string + story_string) 
