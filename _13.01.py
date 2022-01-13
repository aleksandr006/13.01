from tkinter import *
aken=Tk()
Tk=aken()
f1=Frame(aken,width=500,height=500)
f1.pack(side=TOP)
f2=Frame(aken,width=500,height=500)
f2.pack(side=BOTTOM)
Tk = Tk() 
c = Canvas(tk, width=300, height=300, bg="yellow") 
c=Canvas(tk, width=500, height=500, bg="white")
с1=Checkbutton(f1,text = "овал", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
с2=Checkbutton(f1,text = "лица", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
с3=Checkbutton(f1,text = "глаза", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
с4=Checkbutton(f1,text = "нос", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
с5=Checkbutton(f1,text = "рот", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
var=IntVar

tk.mainloop()
c.create_oval((0,0,90,90))
c.create_oval((25,20,35,30))
c.create_oval((50,20,60,30))
c.create_arc((20,40,70,70))
c.create_arc((20,70,70,70), style=CHORD, start=0, extent=150)
c.create_arc((0, 180, 0,0),style=ARC)
c.pack()
tk.mainloop()


aken.pack()