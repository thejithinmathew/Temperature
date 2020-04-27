from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk

def check():
    global location2
    global c
    global f
    s="https://www.google.com/search?q=weather+in"+location2.get()

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    }
    try:
        ht=requests.get(s,headers=headers)
        soup = bs(ht.text, 'lxml')
        loc=soup.find('div', {'id': 'wob_loc'})
        a=soup.find('span', {'id': 'wob_tm'})
        if(loc!=None):
            l.set(loc.text)
        else:
            l.set("Location not Found")
        
        if(a==None):
            f.set("--")
            c.set("--")
        else:
            c1=a.text

            f1=int(c1)*(9/5)
            c1=c1+" degree Celcius"
            c.set(c1)
            f1+=32
            f1=round(f1,2)
            f1=str(f1)+" degree F"
            f.set(f1)
    except:
        l.set("No Internet Connection")
        f.set("--")
        c.set("--")
    
root = tk.Tk()
c=tk.StringVar()
f=tk.StringVar()
l=tk.StringVar()
location2=tk.StringVar()


root.title("Temperature")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)
loca= tk.Entry(frame, textvariable=location2,justify='center')
button_convert = tk.Button(frame, text="Check", command=check)
label_loca = tk.Label(frame, textvariable=l)
label_fahrenheit = tk.Label(frame, textvariable=f)
label_celc = tk.Label(frame, textvariable=c)

loca.grid(row=0, column=1,padx=5,pady=5)
button_convert.grid(row=1, column=1,padx=5,pady=5)
label_loca.grid(row=2, column=1,padx=5,pady=5)
label_celc.grid(row=3, column=0,padx=5,pady=5)
label_fahrenheit.grid(row=3, column=2,padx=5,pady=5)
root.mainloop()





