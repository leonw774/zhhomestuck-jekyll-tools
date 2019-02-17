import os
import io
import re
path = "./_posts/"
for filename in os.listdir(path) :
    file_string = open(path + filename, "r", encoding = 'utf-8').read()
    if re.search("- sbahj", file_string) :
        continue
    elif re.search("- s", file_string) :
        file_string = re.sub("layout: post\n", "layout: post_s\n", file_string)
        io.open(path + filename, 'w', encoding = 'utf-8', newline='\n').write(file_string)
