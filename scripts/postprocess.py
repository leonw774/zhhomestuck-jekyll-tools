import os
import re

POSTPATH = "../zhhomestuck.github.io/p/"
POST_LIST = list(os.listdir(POSTPATH))

def replace_strings():
    print("replacing things in builded pages")
    for filename in POST_LIST:
        try:
            file_string = open(POSTPATH+filename, encoding = 'utf-8-sig').read()
        except: continue
        file_string = re.sub(r"&lt;(?![! ])", "<", file_string) # change every "&lt;" if it is NOT behind "!" or " "
        file_string = re.sub(r"&gt;(?![!;])", ">", file_string) # change every "&gt;" if it is NOT behind "!" or ";"
        file_string = file_string.replace(".html", "") # take out file extention
        file_string = file_string.replace("&amp;", "&")
        file_string = file_string.replace("…", "...")
        open(POSTPATH+filename, "w", encoding = 'utf-8-sig').write(file_string)

if __name__ == "__main__":
    print("post-processing...")
    replace_strings()