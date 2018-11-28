from tkinter import *



top = Tk()

L1Length = IntVar()
L2Length = IntVar()
Lambda = IntVar()
top.geometry("800x600")

L1Scale = Scale(top, orient=HORIZONTAL, variable=L1Length, length=200, to=1000, from_=0, tickinterval=1000, resolution=1)
L1Scale.place(x=150, y=300)
L2Scale = Scale(top, orient=HORIZONTAL, variable=L2Length, length=200, to=1000, from_=0, tickinterval=1000, resolution=1)
L2Scale.place(x=150, y=370)
LambdaScale = Scale(top, orient=HORIZONTAL, variable=Lambda, length=200, to=700, from_=380, tickinterval=700, resolution=1)
LambdaScale.place(x=150, y=440)

LineOneEditLabel = Label(top, text="Comprimento\n de L1")
LineOneEditLabel.place(x=5, y=310)

LineOneEdit = Entry(top, width = 6, relief = FLAT)
LineOneEdit.place(x=100, y=320)

LineTwoEditLabel = Label(top, text="Comprimento\n de L2")
LineTwoEditLabel.place(x=5, y=380)

LineTwoEdit = Entry(top, width = 6, relief = FLAT)
LineTwoEdit.place(x=100, y=390)

LambdaEditLabel = Label(top, text=u"λ")
LambdaEditLabel.place(x=40, y=460)

LambdaEdit = Entry(top, width = 6, relief = FLAT)
LambdaEdit.place(x=100, y=460)

LambdaEditLabel = Label(top, text=u"Índice de\n Refração")
LambdaEditLabel.place(x=20, y=530)

LambdaEdit = Entry(top, width = 6, relief = FLAT)
LambdaEdit.place(x=100, y=540)

top.mainloop()

