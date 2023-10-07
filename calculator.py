from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg


loginForm = Tk()
loginForm.title('Calculator')
loginForm.geometry('400x300')
right = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
down = int(loginForm.winfo_screenheight() / 2 - 200 / 2)
loginForm.geometry('+{}+{}'.format(right, down))
loginForm.resizable(0,0)
loginForm.iconbitmap('images/login.ico')

#function

def resetForm():
    txtNumber1.set("")
    txtNumber2.set("")


def plus():

    Number1 = txtNumber1.get()
    Number2 = txtNumber2.get()
    result=Number1+Number2
    msg.showinfo(':)',result)
    #loginForm.destroy()

def minus():

    Number1 = txtNumber1.get()
    Number2 = txtNumber2.get()
    result=Number1-Number2
    msg.showinfo(':)',result)
    #loginForm.destroy()

def product():

    Number1 = txtNumber1.get()
    Number2 = txtNumber2.get()
    result=Number1*Number2
    msg.showinfo(':)',result)
    #loginForm.destroy()

def devide():

    Number1 = txtNumber1.get()
    Number2 = txtNumber2.get()
    result=Number1/Number2
    msg.showinfo(':)',result)
    #loginForm.destroy()


lblNumber1=Label(loginForm,text='Number1:')
lblNumber1.grid(row=0,column=0,padx=10,pady=10)

txtNumber1=IntVar(value="")
entNumber1=Entry(loginForm,width=20,textvariable=txtNumber1)
entNumber1.grid(row=0,column=1,padx=10,pady=10)

lblNumber2=Label(loginForm,text='Number2:')
lblNumber2.grid(row=1,column=0,padx=10,pady=10)

txtNumber2=IntVar(value="")
entNumber2=Entry(loginForm,width=20,textvariable=txtNumber2)
entNumber2.grid(row=1,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='+',width=10,command=plus)
btnlogin.grid(row=2,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='-',width=10,command=minus)
btnlogin.grid(row=3,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='*',width=10,command=product)
btnlogin.grid(row=4,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='/',width=10,command=devide)
btnlogin.grid(row=5,column=1,padx=10,pady=10)

loginForm.mainloop()
