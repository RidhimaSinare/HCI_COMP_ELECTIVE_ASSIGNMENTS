from tkinter import *

font_tuple = ("Microsoft YaHei UI Light", 23, "bold")

app=Tk()
app.geometry("925x500+300+200")
app.title("Human Computer Interface")
app.configure(bg="#fff")
app.resizable(False,False)

img= PhotoImage(file="login.png")
Label(master=app,image=img,bg="white").place(x=50,y=50)

frame=Frame(master=app,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading= Label(master=frame,text="Sign In",fg="#57a1f8",bg="white",font=font_tuple)
heading.place(x=100,y=5)

user= Entry(master=frame,width=15,fg="black",border=0.2,bg="white",font=('Microsoft YaHei UI Light', 11))
user.place(x=30,y=80)
user.insert(0,'Username')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

code= Entry(master=frame,width=15,fg="black",border=0.2,bg="white",font=('Microsoft YaHei UI Light', 11))
code.place(x=30,y=150)
code.insert(0,'Password')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0.2).place(x=35,y=204)
label=Label(frame,text="Don't have an account ?",fg="black",bg="white",font=('Microsoft YaHei UI Light', 9))
label.place(x=105,y=270)

signup=Button(frame,width=6,text="Sign Up",border=0,bg='white',cursor='hand2',fg='#57a1f8')
signup.place(x=250,y=270)


# Run the main loop
app.mainloop()
