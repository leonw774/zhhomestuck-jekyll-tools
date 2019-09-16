import os
import re
import pandas
from bs4 import BeautifulSoup

for filename in os.listdir("flash_conversion_pages/") :
    print(filename)
    soup = BeautifulSoup(open("flash_conversion_pages/" + filename).read(), 'html.parser')
    head_scripts = soup.find("head").find_all("script", src = re.compile(r".*"))
    body_scripts = soup.find("body").find("script")
    content_container = soup.find(id = "content_container")
    
    head_script_text = "\n".join([str(tag) for tag in head_scripts])
    if body_scripts :
        body_scripts_text = str(body_scripts)
        #body_scripts_text = "\n".join(body_scripts)
    else :
        body_scripts_text = ""
    content_container_text = str(content_container)
    open("flash_conversion_pages/" + filename, "w+").write(head_script_text + "\n" + body_scripts_text + "\n" + content_container_text)
    