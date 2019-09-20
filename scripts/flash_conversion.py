import pandas
from bs4 import BeautifulSoup

def flash2youtube(p) :
    new = open("flash_conversion_pages" + str(p) + ".html").read()
    old = open("../zhhomestuck.github.io/p/" + str(p + 1900) + ".html", "r").read()

flash_conversion = pandas.read_csv("Homestuck com Flash Conversions.csv")
for index, row in flash_conversion.iterrows() :
    p = int(row["URL"].split('/')[4])
    if row["Youtube"] == 1 :
        flash2youtube(p)
    elif row["Static"] == 1 :
        