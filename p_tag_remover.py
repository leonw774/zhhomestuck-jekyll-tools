import io
import os
import re
path = "./zhhomestuck.github.io/p/"
for filenum, filename in enumerate(os.listdir(path)) :
    file_string = open(path + filename, encoding = 'utf-8-sig').read()
    if filenum % 1000 == 0 : print(filenum)
    file_string = re.sub("&lt;(?![! ])", "<", file_string)
    file_string = re.sub("&gt;(?![!])", ">", file_string)
    file_string = re.sub("//end AC code", "", file_string)
    if re.search("<table>", file_string) :
        file_string = re.sub("<table>", "", file_string)
        file_string = re.sub("</table>", "", file_string)
        file_string = re.sub("<tbody>", "", file_string)
        file_string = re.sub("</tbody>", "", file_string)
        file_string = re.sub("<tr>", "", file_string)
        file_string = re.sub("</tr>", "", file_string)
        file_string = re.sub("<td>", "", file_string)
        file_string = re.sub("</td>", "", file_string)
    
    if re.search("AC_FL_RunContent", file_string) :
        file_string = re.sub(r" 'http://cdn.mspaintadventures.com/storyfiles", " 'https://www.homestuck.com/flash", file_string)
    
    file_string = re.sub(r"http.+AC_RunActiveContent\.js", "../AC_RunActiveContent.js", file_string)
    file_string = re.sub(r"(https?://zhhomestuck.blogspot.tw/p/|https?://zhhomestuck.blogspot.com/p/)", "./", file_string)
    file_string = re.sub(r"(https?://zhhomestuck.blogspot.tw/[/0-9]{8}|https?://zhhomestuck.blogspot.com/[/0-9]{8})", "./", file_string)
    open(path + filename, "w", encoding = 'utf-8-sig').write(file_string)
    
