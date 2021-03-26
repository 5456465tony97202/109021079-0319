import requests as reqs

r=reqs.get("http://210.70.80.21/~bs109021079/"
)
print(r.status_code)

#終端機打python -m pip install requests
#再安裝 python -m pip install BeautifulSoup4
