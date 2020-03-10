import os
import io
import re
print("escape markdowns...")
path = "./_posts/"
for filenum, filename in enumerate(os.listdir(path)) :
    file_lines = open(path + filename, "r", encoding = 'utf-8').readlines()
    # find the end of front matter
    end_front_mat = 0
    for id, line in enumerate(file_lines):
        if line == "---\n":
            end_front_mat = id
    yml_string = "".join(file_lines[:end_front_mat])
    story_string = "".join(file_lines[end_front_mat:])
    story_string = story_string.replace("*", "&#42;")
    story_string = story_string.replace("/&#42;", "/*") #css comments
    story_string = story_string.replace("&#42;/", "*/")
    story_string = story_string.replace("&#42;電腦", "*電腦") #roxy's typing animation at 006348
    story_string = story_string.replace("|", "&#124;")
    
    open(path + filename, 'w', encoding = 'utf-8', newline='\n').write(yml_string + story_string) 
