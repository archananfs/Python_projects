from tkinter import *
from tkinter import ttk
import Projects_git.password_generator

length_val =[5,6,7,8,9,10,11,12]

def clicked():
    length=length_variable.get()
    a = Projects_git.password_generator.password_generate(length)
    e1.delete(0, END)
    e1.insert(END, a)

window = Tk()
window.title("Welcome to Password Generator!")


# Output entry

lbl = Label(window, text ="PASSWORD", anchor= CENTER)
lbl.grid(column=0, row=0)

e1_val = StringVar()
e1 = Entry(window,textvariable =e1_val)
e1.grid(column=0,row=1)

# buttons
create_b = Button(window, text='CREATE',width =6, height=1,command=clicked)
create_b.grid(column=1, row=1)

copy_b = Button(window, text='COPY', width =6, height=1)
copy_b.grid(column=2, row=1)

# for length selection
lbl = Label(window, text ="LENGTH", anchor= CENTER)
lbl.grid(column=0, row=2)

length_variable = IntVar()
combo = ttk.Combobox(window, values = length_val, textvariable=length_variable)
combo.grid(column=0, row=3)
window.mainloop()