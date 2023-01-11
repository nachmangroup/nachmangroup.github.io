import os
from datetime import datetime

myfile = open("index.html")
olddate = "7/30/2020"
for line in myfile:
    if "Last Site Update" not in line:
        continue
    olddate = line.split("Update: ")[1].split("<")[0]

newdate = datetime.today().strftime('%m/%d/%Y')
os.system("sed -i 's/"+olddate.replace("/","\/")+"/"+newdate.replace("/","\/")+"/g' *.html")
