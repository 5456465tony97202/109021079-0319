import requests as reqs
from bs4 import BeautifulSoup
req=reqs.get("http://210.70.80.21/~bs109021079/"
)
req.encoding="utf8"  #轉換為"utf8"
if req.status_code == 200:
   soup=BeautifulSoup(req.text,"lxml") #lxml呈現資料的格式
   result1=soup.find_all("li")
   fp=open("out2.txt","w",encoding="utf8")
   i=1 #讓顯示資料較乾淨
   for val in result1:
       text2=val.text.replace("\n"," ")#找到前面的並replace取代後面的
       text3=text2.replace("  ","")
       print(text3) 
       fp.write(text3 +"\n")
    fp.close() 
else:
    print("no page")

#終端機打python -m pip install requests
#再安裝 python -m pip install BeautifulSoup4


