a=[]
from bs4 import BeautifulSoup
import requests
for i in range(int(input("enter a number of palce u want"))):
    b=[];link="https://www.google.com/search?q=longitude of "
    k=input("enter {} palce".format(i))
    try:
     b.append(k)
     page=requests.get(link+k)
     soup =BeautifulSoup(page.content,'html.parser')
     f=str(soup.find("div",{"class":"BNeawe iBp4i AP7Wnd"}).get_text())
     f=f.replace('° N','');f=f.replace('° E','');
     b.extend([float(x) for x in f.split(',')])
    except Exception as e:
     print("error is",e)
    a.append(b)
