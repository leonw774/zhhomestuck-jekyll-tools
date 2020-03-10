import os
from datetime import datetime
print("update index.html")
try:
    file_path = "../zhhomestuck.github.io/p/index.html"
    file = open(file_path, "r", encoding = "utf-8-sig")
except:
    file_path = "../zhhomestuck.github.io/index.html"
    file = open(file_path, "r", encoding = "utf-8-sig")

file_content = file.read()
now_date = datetime.now()
file_content = file_content.replace("date_now", now_date.strftime("%Y-%m-%d"))
file.close

pagename_list = os.listdir("_posts")

update_date = pagename_list[-1][:10]
update_list = [x for x in pagename_list if x[:10]==update_date]
update_list.sort()

update_page_title = ""
with open("_posts/"+update_list[0], "r", encoding = "utf-8-sig") as f:
    for line in f.readlines():
        if line[0:5]=="title":
            update_page_title = line[8:-1]
            break
update_page_link = "/p/" + pagename_list[0][11:17]

file_content = file_content.replace("date_last_update", update_date)
file_content = file_content.replace("update_page_title", update_page_title)
file_content = file_content.replace("update_page_link", update_page_link)
file_content = file_content.replace("update_page_num", str(len(update_list)))

with open(file_path, "w+", encoding = "utf-8-sig") as f :
    f.write(file_content)
