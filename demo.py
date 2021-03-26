import requests as reqs
from bs4 import BeautifulSoup
req=reqs.get("http://210.70.80.21/~bs109021079/"
)
req.encoding="utf8"  #轉換為"utf8"
if req.status_code == 200:
   soup=BeautifulSoup(req.text,"lxml") #lxml呈現資料的格式
   #print(soup)
   result1=soup.find_all("li") 
   print(result1)
else:
    print("no page")

#終端機打python -m pip install requests
#再安裝 python -m pip install BeautifulSoup4


