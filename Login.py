from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    user_id=id.get()
    password=code.get()

    file = open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())
    if user_id in r.keys() and password==r[user_id]: 
        messagebox.showinfo('Valid',"Successfully logged in")
    else:
        messagebox.showerror("Invalid","Invalid username or password!")

#########################################################

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=450,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign In', fg="#57a1f8",bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=4)

#####-------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#####-------------------
def on_enter(e):
    id.delete(0,'end')
def on_leave(e):
    name=id.get()
    if name=="":
        id.insert(0,'User ID')

id = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
id.place(x=30,y=150)
id.insert(0,'User ID')
id.bind('<FocusIn>', on_enter)
id.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
#####-------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=220)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)
#####-------------------

Button(frame,width=39,pady=7,text='Sign In',bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=274)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=330)

sign_up=Button(frame,width=6,text='Sign Up',fg="#57a1f8",bg="white",border=0,cursor='hand2').place(x=215,y=330)

root.mainloop()