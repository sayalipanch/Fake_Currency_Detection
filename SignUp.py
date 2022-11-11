from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title('Sign Up')
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)

def signup():
    username=user.get()
    user_id=id.get()
    password=code.get()
    confirm_password=confirm_code.get()

    if password==confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={user_id:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('Sign Up', 'Signed Up successfully!')
        
        except:
            file=open('datasheet.txt','w')
            pp=str({'User_Id':'password'})
            file.write(pp)
            file.close()        

    else:
        messagebox.showerror('Invalid',"Both the passwords should match")

def sign():
    window.destroy()

img = PhotoImage(file='SignUp.png')
Label(window,image=img,bg='white').place(x=50,y=90)

frame=Frame(window,width=350,height=390,bg="white")
frame.place(x=480,y=50)

heading=Label(frame,text='Sign Up', fg="#57a1f8",bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=1)
####----------

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=70)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=90)

#####-------------------
def on_enter(e):
    id.delete(0,'end')
def on_leave(e):
    name=id.get()
    if name=="":
        id.insert(0,'User ID')

id = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
id.place(x=30,y=130)
id.insert(0,'User ID')
id.bind('<FocusIn>', on_enter)
id.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=150)
#####-------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=190)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=210)
#####-------------------

def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    name=confirm_code.get()
    if name=="":
        confirm_code.insert(0,'Confirm Password')

confirm_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
confirm_code.place(x=30,y=250)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=270)

Button(frame,width=39,pady=7,text='Sign Up',bg="#57a1f8",fg="white",border=0, command=signup).place(x=35,y=300)
label=Label(frame,text="Already have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=350)

sign_in=Button(frame,width=6,text='Sign In',fg="#57a1f8",bg="white",border=0,cursor='hand2',command=sign).place(x=215,y=350)

window.mainloop()