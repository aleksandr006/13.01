from tkinter import *
def lisa_nous():
    if var_nous.get()=="nous":
        c.create_oval((225, 245, 275, 305),width=1, fill="black", outline="black") 
    elif var_nous.get()=="tühi":#нос
        c.create_oval((225, 225, 275, 275),width=1, fill="black", outline="black") 
def lisa_mounth():
    if var_mounth.get()=="mounth":
        c.create_arc((100, 300, 400,400),start=150,extent=150, style=ARC, fill="black",width=10, outline="black")
    elif var_mounth.get()=="tühi":
        c.create_arc((100, 300, 400,400),start=150,extent=150, style=ARC,   fill="thistle",width=10, outline="thistle")
def lisa_eyes():
    if var_eyes.get()=="eyes":
        c.create_oval((300, 100, 400, 200), fill="whitesmoke",width=3, outline="black") 
        c.create_oval((200, 200, 100, 100), fill="whitesmoke",width=3, outline="black") 
    elif var_eyes.get()=="tühi":
        c.create_oval((300, 100, 400, 200),  fill="thistle", outline="thistle") 
        c.create_oval((200, 200, 100, 100),  fill="thistle", outline="thistle") 
def lisa_face():
    if var_face.get()=="face":
        c.create_oval((10, 10, 490, 490),width=5, fill="lavender", outline="black") 
    elif var_face.get()=="tühi":
        c.create_oval((10, 10, 490, 490),width=5, fill="thistle", outline="thistle") 
aken=Tk()
aken.title("Face")
aken.geometry('1000x500')
aken.configure(bg="black")
aken.grab_set()
c = Canvas(aken, width=500, height=500, bg="green")
var_nous=StringVar()
ch_nous=Checkbutton(aken,text="nous", variable=var_nous, onvalue="nous", offvalue="tühi",bg="pink",command=lisa_nous)
var_mounth=StringVar()
ch_mounth=Checkbutton(aken,text="mounth", variable=var_mounth, onvalue="mounth", offvalue="tühi",bg="yellow",command=lisa_mounth)
var_eyes=StringVar()
ch_eyes=Checkbutton(aken,text="eyes", variable=var_eyes, onvalue="eyes", offvalue="tühi",bg="blue",command=lisa_eyes)
var_face=StringVar()
ch_face=Checkbutton(aken,text="face", variable=var_face, onvalue="face", offvalue="tühi",bg="green",command=lisa_face)

ch_nous.pack(side=RIGHT)
ch_mounth.pack(side=RIGHT)
ch_eyes.pack(side=RIGHT)
ch_face.pack(side=RIGHT)
c.pack(side=RIGHT)
ch_nous.pack(side=RIGHT)
aken.mainloop()

