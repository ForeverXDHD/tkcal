from tkinter import *

window = Tk()

window.geometry("450x350")
label = Label(window,text="Tkinter basic calculator!")

label.pack()
entry = Entry(window,text="")
entry.pack()

#entry2 = Entry(window,text="")
#entry2.pack()
label2 = Label(window)

def cmd():
    e = (str(eval(entry.get())))
    label2 = Label(window,text=e)
    label2.pack()
button = Button(window,text="return",command=cmd)
button.pack()

window.mainloop()