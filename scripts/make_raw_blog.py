import os
import re
print("make blog-raw.txt")
postpath = "_posts/"
pagepath = "_pages/"

def strip_xml_tag(content_string):
    content_string += "\n"
    content_string = re.sub(r"(<br>)|(<br/>)|(<br />)|(</br>)", "\n", content_string)
    
    # remove non-displayed HTML elements
    content_string = re.sub(r"<!--(?:(?!<!--|-->)[\S\s])*-->", "", content_string)
    content_string = re.sub(r"<script(?:(?!<script|</script>)[\S\s])*</script>", "", content_string)
    content_string = re.sub(r"<style(?:(?!<style|</style>)[\S\s])*</style>", "", content_string)
    content_string = re.sub(r"<button(?:(?!<button|</button>)[\S\s])*</button>", "", content_string)
    
    # remove XML tags
    content_string = re.sub(r"<[^<^>]+>", "", content_string)
    
    content_string = re.sub(r"\n[\s]+", "\n", content_string)
    content_string = re.sub(r" +", " ", content_string)
    return content_string

replace_dict = {
"&nbsp;" : " ",
"&gt;" : ">",
"&lt;" : "<",
"&amp;" : "&",
"&#42;" : "*",
"&#124;" : "|",
"&#65292;" : "，",
"&#12290;" : "。",
"&#65281;" : "！",
"&#65311;" : "？",
"&#12300;" : "「",
"&#12301;" : "」",
}

postname_list = sorted(list(os.listdir(postpath)))
content_string = ""

blog_raw = open("blog-raw.txt", 'w+', encoding = 'utf-8-sig')
for file_i, filename in enumerate(postname_list):
    old_file_lines = open(postpath + filename, 'r', encoding = 'utf-8-sig').readlines()[1:]
    
    # get title & find the end of front matter then remove front matter
    new_lines = []
    end_front_mat = 0
    for id, line in enumerate(old_file_lines):
        if "title:" in line:
            new_lines.append(old_file_lines[id][7:])
        if line == "---\n":
            end_front_mat = id+1
    new_lines.extend(old_file_lines[end_front_mat:])
    
    content_string = "".join(new_lines)
    content_string = strip_xml_tag(content_string)
    for key in replace_dict.keys():
        content_string = re.sub(key, replace_dict[key], content_string)
    blog_raw.write(content_string)
    blog_raw.write("\n")

pagename_list = list(os.listdir(pagepath))

blog_pages = open("blog-pages.txt", 'w+', encoding = 'utf-8-sig')
for file_i, filename in enumerate(pagename_list):
    old_file_lines = open(pagepath + filename, 'r', encoding = 'utf-8-sig').readlines()[1:]
    
    # get title & find the end of front matter then remove front matter
    new_lines = []
    end_front_mat = 0
    for id, line in enumerate(old_file_lines):
        if "title:" in line:
            new_lines.append(old_file_lines[id][7:])
        if line == "---\n":
            end_front_mat = id+1
    new_lines.extend(old_file_lines[end_front_mat:])

    content_string = "".join(new_lines)
    content_string = strip_xml_tag(content_string)
    for key in replace_dict.keys():
        content_string = re.sub(key, replace_dict[key], content_string)
    blog_pages.write(content_string)
    blog_pages.write("\n")

blog_pages.close()
blog_raw.write(open("blog-pages.txt", 'r', encoding = 'utf-8-sig').read())
blog_raw.close()
