import tkinter as tk
from tkinter import messagebox




import random

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char



    password_entry.insert(0, password)




window = tk.Tk()
window.title("Password Manager")
window.config(padx = 0 , pady = 20)

def add_data():

    website = website_entry.get()
    email = email_entry.get()
    passwordo = password_entry.get()

    is_ok = messagebox.askokcancel(title = 'Title', message = f'These are the details that you entered: \n Email: {email} \n Password: {passwordo} \n Is it ok to save?')


    if len(passwordo) == 0 or len(website) == 0:
        messagebox.showinfo(title = "Oops!", message = "Please make sure you haven't left anything empty")
    else:
        if is_ok:
            with open("data.txt", 'a') as data:

                data.write(f"{website} | {email} | {passwordo}")








blank = tk.Label(text = "                                                     ", height= 3)
blank.grid(column = 1, row = 0)

website_label = tk.Label(text = "Website:", font = ("Ariel" , 11 , "italic"))
website_label.grid(column = 0 , row = 1)
email_label = tk.Label(text = "Email / Username:", font = ("Ariel" , 11 , "italic"))
email_label.grid(column = 0 , row = 2)
password_label = tk.Label(text = "Password:", font = ("Ariel" , 11 , "italic"))
password_label.grid(column = 0 , row = 3)

website_entry = tk.Entry()
website_entry.grid(column = 1, row = 1)
website_entry.focus()
email_entry = tk.Entry()
email_entry.grid(column = 1, row = 2)
password_entry = tk.Entry()
password_entry.grid(column = 1, row = 3)

generate_passwordo = tk.Button(text = "Generate Password", command = generate_password)
generate_passwordo.grid(column = 2, row = 3)
add = tk.Button(text = "Add", width = 30, command = add_data)
add.grid(row = 4 , column = 1)





window.mainloop()