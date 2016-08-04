from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
def home(request):
    
    r1 = requests.get("http://trends24.in/")
    soup = BeautifulSoup(r1.text,"html.parser")
    countries_text=[]
    s=[]
    countries=soup.find_all("ul",{'class':'suggested-locations__list'})
    for a in countries:
        s=a.find_all("li")
    r=0
    for k in s:
        countries_text.insert(r,k.text)
        r=r+1
    context={'countries':countries_text}
    return render(request,"app/home.html",context)


# Create your views here.
