from tkinter import *
import math as m

root=Tk()
def calc(x):
    global data
    data=data+x
    s1.set(data)
def clr():
    global data
    data=''
    s1.set(data)
def eql():
    global data
    res=eval(s1.get())
    data=str(res)
    s1.set(data)

def sqr():
    
    global data
    x=int(s1.get())
    data=str(x**2)
    s1.set(data)
 
def cube():
    global data
    x=int(s1.get())
    data=str(x**3)
    s1.set(data)
def factorial():
    global data
    x=int(s1.get())
    data=str(m.factorial(x))
    s1.set(data)
def bs():
    global data
    x=s1.get()
    l=len(x)
    data=x[0:l-1]
    s1.set(data)
    
data=''  
s1=StringVar()
Entry(root,textvariable=s1).grid(row=0,columnspan=4)
Button(root,text='7',font='arial 12', bd=5,bg='black',fg='white' ,command=lambda:calc('7')).grid(row=2,column=0)
Button(root,text='8',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('8')).grid(row=2,column=1)
Button(root,text='9',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('9')).grid(row=2,column=2)
Button(root,text='+',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('+')).grid(row=2,column=3)

Button(root,text='4',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('4')).grid(row=3,column=0)
Button(root,text='5',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('5')).grid(row=3,column=1)
Button(root,text='6',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('6')).grid(row=3,column=2)
Button(root,text='-',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('-')).grid(row=3,column=3)

Button(root,text='1',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('1')).grid(row=4,column=0)
Button(root,text='2',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('2')).grid(row=4,column=1)
Button(root,text='3',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('3')).grid(row=4,column=2)
Button(root,text='*',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('*')).grid(row=4,column=3)

Button(root,text='c',font='arial 12', bd=5,bg='black',fg='white',command=clr).grid(row=5,column=0)
Button(root,text='=',font='arial 12', bd=5,bg='black',fg='white',command=eql).grid(row=5,column=1)
Button(root,text='0',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('0')).grid(row=5,column=2)
Button(root,text='/',font='arial 12', bd=5,bg='black',fg='white',command=lambda:calc('/')).grid(row=5,column=3)

Button(root,text='sq',font='arial 12', bd=5,bg='black',fg='white',command=sqr).grid(row=6,column=0)
Button(root,text='cu',font='arial 12', bd=5,bg='black',fg='white',command=cube).grid(row=6,column=1)
Button(root,text='f',font='arial 12', bd=5,bg='black',fg='white',command=factorial).grid(row=6,column=2)
Button(root,text='bs',font='arial 12', bd=5,bg='black',fg='white',command=bs).grid(row=6,column=3)


root.mainloop()

