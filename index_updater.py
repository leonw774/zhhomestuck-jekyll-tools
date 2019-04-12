import os
from datetime import datetime

file_content = open("index_template.html", "r+", encoding = "utf-8-sig").read()

now_date = datetime.now()
file_content = file_content.replace("now_date", now_date.strftime("%Y-%m-%d"))

pagename_list = os.listdir("_posts")
pagename_list.sort()
file_content = file_content.replace("last_update_date", pagename_list[-1][:10])

with open("index_updated.html", "w+", encoding = "utf-8-sig") as f :
    f.write(file_content)