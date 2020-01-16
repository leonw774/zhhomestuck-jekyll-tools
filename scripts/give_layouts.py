import os
import io
import re
print("give layouts in _posts")
path = "./_posts/"
tags = ["s", "trickster", "x2combo"]
layoutname = ["post_s", "post_trickster", "post_x2combo"]
for filename in os.listdir(path) :
    file_string = open(path + filename, "r", encoding = 'utf-8').read()
    #if re.search("- sbahj", file_string) :
    #    continue
    for index, tag in enumerate(tags) :
        if re.search("- " + tag, file_string) :
            file_string = re.sub("layout: post\n", "layout: " + layoutname[index] + "\n", file_string)
            io.open(path + filename, 'w', encoding = 'utf-8', newline='\n').write(file_string)
