from tkinter import *
sobhan = Tk()
sobhan.geometry("500x600")
sobhan.title("sobhan")
sobhan.resizable(False,False)
def number ():
    global label2
    z = int1.get() + int2.get()
    lable2Text.set(z)

    
int1 = IntVar()
int2 = IntVar()
label1 = Label(sobhan, text="Welcome My App")
label1.pack()
entry1 = Entry(sobhan,textvariable=int1)
entry1.pack()
entry2 = Entry(sobhan,textvariable=int2).pack()
button1 = Button(sobhan, text="click me!", command=number).pack()
lable2Text = IntVar()
label2 = Label(sobhan,textvariable=lable2Text).pack()

sobhan.mainloop()