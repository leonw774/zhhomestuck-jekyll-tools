# encoding = utf-8
import io
import os
import re
path = ""
config_file = open("_config.yml", "r", encoding = "utf-8-sig")
for line in config_file.readlines() :
    a = line.split()
    if a[0] == "destination:" :
        path = a[1] + '/'
        break
for filenum, filename in enumerate(os.listdir(path)) :
    file_string = open(path + filename, encoding = 'utf-8-sig').read()
    if filenum % 1000 == 0 : print(filenum)
    file_string = re.sub("&lt;(?![! ])", "<", file_string) # change every "&lt;" if it is NOT behind "!" or " "
    file_string = re.sub("&gt;(?![!;])", ">", file_string) # change every "&gt;" if it is NOT behind "!" or ";"
    file_string = re.sub("&amp;", "&", file_string)
    file_string = file_string.replace("//end AC code", "")
    file_string = file_string.replace("…", "...")
    #if re.search("<table>", file_string) :
    #    file_string = re.sub("</?table>|</?tbody>|</?tr>|</?td>", "", file_string)
    
    if re.search("AC_FL_RunContent", file_string) :
        file_string = file_string.replace(r" 'http://cdn.mspaintadventures.com/storyfiles", " 'https://www.homestuck.com/flash")
    
    file_string = re.sub(r"http://zhhomestuck.github.io", "https://zhhomestuck.github.io", file_string)
    # sources host on github was non-security linked, change it to security
    file_string = re.sub(r"http://cdn.mspaintadventures.com/storyfiles/hs2/", "https://www.homestuck.com/images/storyfiles/hs2/", file_string)
    # change mpsa link to homestuck.com
    file_string = re.sub(r"http.+AC_RunActiveContent\.js", "../AC_RunActiveContent.js", file_string)
    # redirect mpsa AC.js to our own
    file_string = re.sub(r"https?://zhhomestuck.blogspot.(tw|com)/p/", "./", file_string)
    # redirect site name
    file_string = re.sub(r"https?://zhhomestuck.blogspot.(tw|com)/[/0-9]{8}", "./", file_string)
    # redirect site name
    file_string = re.sub(r"\.html", "", file_string)
    # take out file extention
    open(path + filename, "w", encoding = 'utf-8-sig').write(file_string)
    
