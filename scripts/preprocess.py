import io
import os
import re

POSTPATH = "_posts/"
PAGEPATH = "_pages/"
POST_LIST = list(os.listdir(POSTPATH))
PAGE_LIST = list(os.listdir(PAGEPATH))
COMBINED_FILEPATH_LIST = [POSTPATH+n for n in sorted(POST_LIST)] + [PAGEPATH+n for n in sorted(PAGE_LIST)]

def index_check():
    print("checking continuity of p-values of post...")
    # check if the p value is right
    pre_p = 0
    cur_p = 0
    for pname in POST_LIST:
        cur_p = int(pname[11:17])
        if pre_p != 0 and cur_p != pre_p + 1:
            print("p value error at", pname)
        pre_p = cur_p
    
def strip_xml_tag(string):
    string += "\n"
    string = re.sub(r"(<br>)|(<br/>)|(<br />)|(</br>)", "\n", string)
    
    # remove non-displayed HTML elements
    string = re.sub(r"<!--(?:(?!<!--|-->)[\S\s])*-->", "", string)
    string = re.sub(r"<script(?:(?!<script|</script>)[\S\s])*</script>", "", string)
    string = re.sub(r"<style(?:(?!<style|</style>)[\S\s])*</style>", "", string)
    string = re.sub(r"<button(?:(?!<button|</button>)[\S\s])*</button>", "", string)
    
    # remove XML tags
    string = re.sub(r"<[^<^>]+>", "", string)
    
    string = re.sub(r"\n[\s]+", "\n", string)
    string = re.sub(r" +", " ", string)
    return string

def make_plain_blog():
    print("making blog-plain.txt...")
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
    
    transcript_page_list = []
    
    content_string = ""
    blog_plain = io.open("blog-plain.txt", 'w+', encoding='utf-8')
    for filepath in COMBINED_FILEPATH_LIST:
        if filepath in transcript_page_list:
            break
        file_lines = io.open(filepath, 'r', encoding='utf-8').readlines()[1:]
        # get title & find the end of front matter then remove front matter
        title_line = ""
        tidied_lines = []
        end_front_mat = 0
        for i, line in enumerate(file_lines):
            if "title:" in line:
                title_line = file_lines[i][7:]
            if line == "---\n":
                end_front_mat = i+1
        
        content_string = "".join(file_lines[end_front_mat:])
        # check if it is game; true then use page content
        if "純文字版本" in content_string:
            for name in PAGE_LIST:
                if name in content_string:
                    page_lines = io.open(PAGEPATH+name, 'r', encoding='utf-8').readlines()[6:]
                    content_string = title_line + "".join(page_lines)
                    transcript_page_list.append(PAGEPATH+name)
                    break
        else:
            content_string = title_line + content_string
        
        content_string = strip_xml_tag(content_string)
        for key in replace_dict.keys():
            content_string = re.sub(key, replace_dict[key], content_string)
        blog_plain.write(content_string)
        blog_plain.write("\n")
    blog_plain.close()
# end def make_raw_blog

def give_layouts():
    print("giving layouts in _posts...")
    tags = ["s", "sbahj", "trickster", "x2combo"]
    layoutname = ["post_s", "post_sbahj", "post_trickster", "post_x2combo"]
    for filename in POST_LIST :
        file_string = io.open(POSTPATH+filename, "r", encoding = 'utf-8').read()
        #if re.search("- sbahj", file_string) :
        #    continue
        for index, tag in enumerate(tags) :
            if re.search("- "+tag+"\n", file_string):
                suffix = ""
                if tag == "x2combo":
                    if int(filename[11:17]) % 2 == 0:
                        suffix = "_left"
                    else:
                        suffix = "_right"
                file_string = re.sub("layout: post\n", "layout: "+layoutname[index]+suffix+"\n", file_string)
                io.open(POSTPATH+filename, 'w', encoding='utf-8', newline='\n').write(file_string)

def escape_markdowns():       
    print("escape markdowns...")
    for filename in POST_LIST:
        file_lines = io.open(POSTPATH+filename, "r", encoding='utf-8').readlines()
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
        io.open(POSTPATH+filename, 'w', encoding='utf-8', newline='\n').write(yml_string+story_string) 

def replace_strings():
    print("replacing strings and links...")
    for filename in POST_LIST:
        file_string = io.open(POSTPATH+filename, encoding='utf-8').read()
        
        #if re.search("<table>", file_string) :
        #    file_string = re.sub("</?table>|</?tbody>|</?tr>|</?td>", "", file_string)
        
        if re.search("AC_FL_RunContent", file_string):
            file_string = file_string.replace(" 'http://cdn.mspaintadventures.com/storyfiles", " 'https://www.homestuck.com/flash")
        
        # sources host on github was non-security linked, change it to security
        file_string = file_string.replace("http://zhhomestuck.github.io", "https://zhhomestuck.github.io")
        
        # change mpsa link to homestuck.com
        file_string = re.sub("https?://(cdn|www).mspaintadventures.com/storyfiles/hs2/", "https://www.homestuck.com/images/storyfiles/hs2/", file_string)
        
        # redirect mpsa AC.js to our own
        file_string = re.sub(r"http.+AC_RunActiveContent\.js\"", "../AC_RunActiveContent.js\"", file_string)
        
        # redirect site name
        file_string = re.sub(r"https?://zhhomestuck.blogspot.(tw|com)/(p|[/0-9]{7})/", "./", file_string)
        
        io.open(POSTPATH+filename, "w", encoding='utf-8', newline='\n').write(file_string)

if __name__ == "__main__":
    print("pre-processing...")
    index_check()
    make_plain_blog()
    give_layouts()
    escape_markdowns()
    replace_strings()
