# simple password generator with a GUI using the Tkinter and pyperclip modules

import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# calculation function
def low():
	entry.delete(0, END)

	# sets the password length
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	# if strength is set to low
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	# if strength is set to medium
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	# if strength is set to strong
	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")


# generates the password
def generate():
	password1 = low()
	entry.insert(10, password1)


# copies the password to the clipboard
def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


# main functions

# creates the GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# gives a title to your GUI window
root.title("Random Password Generator")

# creates the label and an entry to show the password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# creates the label for the length of the password
c_label = Label(root, text="Length")
c_label.grid(row=1)

# create the button 'Copy' which will copy the password to the clipboard and generates the password
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# radio buttons for the strenth of the password, default strength is set to medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)

# combo box for the length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

# starts the GUI
root.mainloop()