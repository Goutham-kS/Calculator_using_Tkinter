from tkinter import *
app=Tk()
app.geometry("900x700")
app.title("calculator")

inputA=IntVar()
inputB=IntVar()
inputC=IntVar()
def Addition():
    a=inputA.get()
    b=inputB.get()
    result=a+b
    inputC.set(result)
def subtraction():
    a=inputA.get()
    b=inputB.get()
    result=a-b
    inputC.set(result)
def multiplication():
    a=inputA.get()
    b=inputB.get()
    result=a*b
    inputC.set(result)
def division():
    a=inputA.get()
    b=inputB.get()
    result=a/b
    inputC.set(result)
##############################################
l1=Label(app,text="number 1",font=("times new roman","20","bold"),fg="black",bg="white").place(x=50,y=100)
l2=Label(app,text="number 2",font=("times new roman","20","bold"),fg="black",bg="white").place(x=50,y=150)
l3=Label(app,text="Result",font=("times new roman","20","bold"),fg="black",bg="white").place(x=50,y=400)
e1=Entry(app,font=("times new roman","20","bold"),fg="black",bg="white",textvariable=inputA).place(x=200,y=100)
e2=Entry(app,font=("times new roman","20","bold"),fg="black",bg="white",textvariable=inputB).place(x=200,y=150)
e3=Entry(app,font=("times new roman","20","bold"),fg="black",bg="white",textvariable=inputC).place(x=150,y=400)
b1=Button(app,text="+",font=("times new roman","20","bold"),fg="black",bg="white",command=Addition).place(x=100,y=200)
b2=Button(app,text="-",font=("times new roman","20","bold"),fg="black",bg="white",command=subtraction).place(x=200,y=200)
b3=Button(app,text="*",font=("times new roman","20","bold"),fg="black",bg="white",command=multiplication).place(x=300,y=200)
b4=Button(app,text="/",font=("times new roman","20","bold"),fg="black",bg="white",command=division).place(x=400,y=200)
