from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = 'Courier'
FONT_TYPE = 'bold'
SIZE = 10

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)

  password = ''.join(password_list)

  password_input.insert( 0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_infos():
  
  if len(website_input.get()) == 0 or len(password_input.get()) == 0:
    messagebox.showwarning(title='Error!', message='Empty Input!\nmake sure to fill the form')
  else:
  
    is_ok = messagebox.askokcancel(title=website_input.get(), message=f'These are the details entered: \n Email: {username_input.get()}\n Password: {password_input.get()}\n Would you like to save it?')
    
    if is_ok:
    
      with open ('data.txt', 'a') as data:
        data.write(f'{website_input.get()} | {username_input.get()} | {password_input.get()} \n')
      
      website_input.delete(0, END)
      password_input.delete(0, END)
      website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

lock_img = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column=1, row=0)

#LABELS
website = Label(text='Website: ', font=(FONT_NAME, SIZE, FONT_TYPE))
website.grid(column=0, row=1)

user_name = Label(text='Email/Username: ', font=(FONT_NAME, SIZE, FONT_TYPE))
user_name.grid(column=0, row=2)

password = Label(text='Password: ', font=(FONT_NAME, SIZE, FONT_TYPE))
password.grid(column=0, row=3)

#ENTRY
website_input= Entry(width=53)
website_input.grid(column=1, row=1, columnspan=2)
website_input.config(borderwidth=0)
website_input.focus()

username_input= Entry(width=53)
username_input.grid(column=1, row=2, columnspan=2)
username_input.config(borderwidth=0)
username_input.insert( 0, 'marcus@gmail.com')

password_input= Entry( width=34)
password_input.grid(row=3, column=1)
password_input.config(borderwidth=0)

#BUTTON
pass_gen = Button(text='Generate Password', command=generate_password)
pass_gen.grid(row=3, column=2)
pass_gen.config(borderwidth=0, fg='blue')

pass_gen = Button(text='Add', width=40, font=(FONT_NAME, SIZE, FONT_TYPE), command=save_infos)
pass_gen.grid(column=1, row=4, columnspan=2)
pass_gen.config(borderwidth=0, fg='green')

window.mainloop()