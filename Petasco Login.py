from tkinter import *


petasco =Tk()
petasco.title('LOGIN')
petasco.geometry('350x450')
petasco.config(bg='black')

lbl = Label(petasco, text='LOGIN', font=('Algeria', 25, 'bold'), bg='black', fg='red')
lbl.place(x=100, y=0)

#======================================= login label =====================================
loginlbl = Label(petasco, text='Username:',font=('times', 15, 'bold'), fg='white', bg='black' )
loginlbl.place(x=10, y=65)

Username = StringVar()
loginentry = Entry(petasco, font=('times', 14, 'bold'), bd=4)
loginentry.focus_set()
loginentry.place(x=10, y=95)

# ================================ password label ===========================================
passwordlbl = Label(petasco, text='Password:', font=('times', 15, 'bold'),fg='white', bg='black')
passwordlbl.place(x=10, y=150)

password = StringVar()
passwordentry = Entry(petasco,textvariable=password, font=('times', 14, 'bold'), bd=4, show='*')
passwordentry.place(x=10,y=180)


def Loginbtn():
    if Username.get() == username and password.get() == Password:
        Message.event_info(petasco,'Success')
        #Message.config(text='Sucess')


#============================ login buttton =============================
loginbtn = Button(petasco, text='Login',command=Loginbtn, font=('Arial', 20, 'bold'), bg='gold', fg='black', width=8)
loginbtn.place(x=30, y=240, height=35)

newlbl =Label(petasco, text='New Here?', font=('times', 10, 'italic'), fg='red',bg='black')
newlbl.place(x=50, y=400)

sign_up_btn = Button(petasco, text='Sign Up', font=('Arial', 18, 'bold'), fg='black', bg='gold')
sign_up_btn.place(x=120, y=400, height=35)

username = 'Petasco'
Password = '2004'
petasco.resizable(False,False)
petasco.mainloop()