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
        
    file_string = re.sub(r"(/zhhomestuck.blogspot.tw/p/|/zhhomestuck.blogspot.com/p/)", "./", file_string)
    file_string = re.sub(r"(/zhhomestuck.blogspot.tw/[/0-9]{8}|/zhhomestuck.blogspot.com/[/0-9]{8})", "./", file_string)
    open(path + filename, "w", encoding = 'utf-8-sig').write(file_string)
    
