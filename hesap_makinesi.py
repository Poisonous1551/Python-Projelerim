from tkinter import *
import time


def yaz(x):
    al=len(text.get())
    text.insert(al,str(x))
    
    
hesap=5
s1=0
    
def islemler(x):
    global hesap
    global s1

    hesap=x    
    s1=float(text.get())
    text.delete(0,'end')
    
s2=0
def hesapla():
    global s2
    
    s2=float(text.get())
    
    global hesap
    
    if hesap==0:
        cevap=s1+s2
    elif hesap==1:
        cevap=s1-s2
    elif hesap==2:
        cevap=s1/s2
    elif hesap==3:
        cevap=s1*s2
    text.delete(0,'end')
    text.insert(0,str(cevap))
    time.sleep(5)
    text.delete(0,'end')
    
        
    
window=Tk()

window.geometry("500x500")

text=Entry(font='verdana 14 bold',width=13,justify=RIGHT)
text.place(x=20,y=20)

b=[]

for i in range(1,10):
    b.append(Button(text=str(i),font='verdana 14 bold',command=lambda x=i:yaz(x),width=2))
    
sayı=0
    
for i in range(0,3):
    for j in range(0,3):
        b[sayı].place(x=20+j*50,y=50+i*50)
        sayı +=1
        
islem=[]

for i in range(0,4):
    islem.append(Button(font='verdana 14 bold',width=2,command=lambda x=i:islemler(x)))
    
islem[0]['text']='+'
islem[1]['text']='-'
islem[2]['text']='/'
islem[3]['text']='x'

for i in range(0,4):
    islem[i].place(x=170,y=50+i*50)


dot=Button(font='verdana 14 bold',text='.',command=lambda x='.':yaz(x),width=2)
dot.place(x=20,y=200)

null=Button(font='verdana 14 bold',text='0',command=lambda x=0:yaz(x))
null.place(x=70,y=200)

sonuc=Button(font='verdana 14 bold',text='=',fg='RED',command=hesapla)
sonuc.place(x=120,y=200)
        

window.mainloop()