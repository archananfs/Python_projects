from tkinter import *
from PyDictionary import PyDictionary
dictionary = PyDictionary()


def dict_translate():
    word = e1_value.get()
    list1.delete(0, END)
    meaning = dictionary.meaning(word)
    for key, value in meaning.items():
        if type(value) == list:
            for line in value:

                list1.insert(END, line)
        else:
            list1.delete(0, END)
            list1.insert(END, value)


def clear_text():
    e1.delete(0,END)


window = Tk()
window.title("Welcome!")


# Lables

labl_1 = Label(window, text="Enter the Word")
labl_1.grid(column=0, row=0)

labl_2 = Label(window, text="Output")
labl_2.grid(column=0, row=2)

# entry
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(column=0, row=1)

# Buttons
btn1 = Button(window, text="Meaning", command=dict_translate)
btn1.grid(column=1, row=1)

# Clear Button
btn2 = Button(window, text="Clear", command=clear_text)
btn2.grid(column=2, row=1)

#Output window
list1 = Listbox(window, height=10, width=100)
list1.grid(column=0, row=3, rowspan=6, columnspan=2)

#scrollbar
sb1 = Scrollbar(window)
sb1.grid(column=2, row=3, rowspan=6)

list1.configure(yscrollcommand=sb1)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>')

window.mainloop()
