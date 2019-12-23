import os
from datetime import datetime

file_path = "../zhhomestuck.github.io/p/index.html"
file = open(file_path, "r", encoding = "utf-8-sig")
if file:
    file_content = file.read()
else:
    file_path = "../zhhomestuck.github.io/index.html"
    file = open(file_path, "r", encoding = "utf-8-sig")
    if file:
        file_content = file.read()
    else:
        exit()

now_date = datetime.now()
file_content = file_content.replace("now_date", now_date.strftime("%Y-%m-%d"))

pagename_list = os.listdir("_posts")
pagename_list.sort()
file_content = file_content.replace("last_update_date", pagename_list[-1][:10])

with open(file_path, "w+", encoding = "utf-8-sig") as f :
    f.write(file_content)