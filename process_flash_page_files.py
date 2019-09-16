import os
import re
import pandas
import requests
from bs4 import BeautifulSoup

flash_conversion_pages = pandas.read_csv("Homestuck com Flash Conversions.csv")
ytid_file = open("flash_conversion_pages/youtubeids.csv", "w+", encoding = "utf-8-sig")
altimg_file = open("flash_conversion_pages/altimgsrc.csv", "w+", encoding = "utf-8-sig")
for index, row in flash_conversion_pages.iterrows() :
    p = row["URL"].split('/')[4]
    print(p)
    r = requests.get(row["URL"])
    soup = BeautifulSoup(r.text, 'html.parser')
    
    if row["Youtube"] == 1 :
        ytid_string = soup.find(id = "o_flash-container").find("script").string
        if ytid_string == None : continue
        i = ytid_string.find("\'youtubeid")
        ytid_string = ytid_string[i : i + 26] + "\n"
        ytid_file.write(p + "," + ytid_string)
    elif row["Static"] == 1:
        altimg_string = soup.find(id = "o_flash-container").find("script").string
        if altimg_string == None : continue
        fr = altimg_string.find("\'altimgsrc")
        to = altimg_string.find("gif") + 4
        altimg_string = altimg_string[fr : to] + "\n"
        altimg_file.write(p + "," + altimg_string)
    else :  
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
        open("flash_conversion_pages/" + p + ".xml", "w+", encoding = "utf-8-sig").write(head_script_text + "\n" + body_scripts_text + "\n" + content_container_text)
    