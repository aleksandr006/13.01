from tkinter import *

def lisa_nous():
    if var_nous.get()=="nous":
        c.create_oval((225, 245, 275, 305),width=3, fill="crimson", outline="black") #нос
    elif var_nous.get()=="tühi":
        c.create_oval((225, 225, 275, 275),width=3, fill="thistle", outline="pink") #нос
def lisa_suu():
    if var_suu.get()=="mounth":
        c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC, fill="black",width=10, outline="black")
    elif var_suu.get()=="tühi":
        c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC,   fill="thistle",width=10, outline="thistle")
def lisa_eyes():
    if var_eyes.get()=="eyes":
        c.create_oval((300, 100, 400, 200), fill="whitesmoke",width=3, outline="black") #првый глаз
        c.create_oval((200, 200, 100, 100), fill="whitesmoke",width=3, outline="black") #левый глаз
    elif var_eyes.get()=="tühi":
        c.create_oval((300, 100, 400, 200),  fill="thistle", outline="thistle") #првый глаз
        c.create_oval((200, 200, 100, 100),  fill="thistle", outline="thistle") #левый глаз
def lisa_nao():
    if var_nao.get()=="face":
        c.create_oval((10, 10, 490, 490),width=5, fill="lavender", outline="black") #лицо
    elif var_nao.get()=="tühi":
        c.create_oval((10, 10, 490, 490),width=5, fill="thistle", outline="thistle") #лицо
aken=Tk()
aken.title("Face")
aken.geometry('1000x500')
aken.configure(bg="black")
aken.grab_set()
c = Canvas(aken, width=500, height=500, bg="green")
var_nous=StringVar()
ch_nous=Checkbutton(aken,text="nous", variable=var_nous, onvalue="nous", offvalue="tühi",bg="pink",command=lisa_nous)
var_suu=StringVar()
ch_suu=Checkbutton(aken,text="mounth", variable=var_suu, onvalue="mounth", offvalue="tühi",bg="yellow",command=lisa_suu)
var_eyes=StringVar()
ch_eyes=Checkbutton(aken,text="eyes", variable=var_eyes, onvalue="eyes", offvalue="tühi",bg="blue",command=lisa_eyes)
var_nao=StringVar()
ch_nao=Checkbutton(aken,text="face", variable=var_nao, onvalue="face", offvalue="tühi",bg="green",command=lisa_nao)



ch_nous.pack(side=RIGHT)
ch_suu.pack(side=RIGHT)
ch_eyes.pack(side=RIGHT)
ch_nao.pack(side=RIGHT)
c.pack(side=RIGHT)
ch_nous.pack(side=RIGHT)
aken.mainloop()

