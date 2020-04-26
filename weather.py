from bs4 import BeautifulSoup as bs
import requests
from tkinter import *
from tkinter import messagebox
location=input("Enter Location: ")
s="https://www.google.com/search?q=weather+in"+location

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
}

ht=requests.get(s,headers=headers)
soup = bs(ht.text, 'lxml')
loc=soup.find('div', {'id': 'wob_loc'})
a=soup.find('span', {'id': 'wob_tm'})
if(a.text==None):
    temp="Unable to find Temperature in "+location+"! Try Again!"
else:
    temp="The Temperature is: "+a.text+" degree Celcius in "+loc.text+"!"
Tk().withdraw()
messagebox.showinfo(title="Temperature",message=temp)
