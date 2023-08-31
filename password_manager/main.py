from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

FONT_NAME = "Arial"
FILE_NAME = "data.json"
DEFAULT_USERID = "example_email@gmail.com"


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def save():
    # This function saves the data to a file
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email}\nPassword: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            try:
                with open(FILE_NAME, "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(FILE_NAME, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open(FILE_NAME, "w") as data_file:
                    # Saving the updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, DEFAULT_USERID)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get().capitalize()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Nothing to search. Please enter a valid entry.")
    else:
        try:
            with open(FILE_NAME, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No datafile found.")
        else:
            if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']} "
                                                                f"\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"Data for the website {website} doesn't exist.")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# the canvas widget
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# label widgets
website_label = Label(text="Website:", font=(FONT_NAME, 15),)
website_label.grid(row=1, column=0)
userid_label = Label(text="Email/Username:", font=(FONT_NAME, 15),)
userid_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=(FONT_NAME, 15))
password_label.grid(row=3, column=0)

# entry widgets
website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, DEFAULT_USERID)
password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

# button widgets
gen_pass = Button(text="Generate Password", command=gen_password, width=13)
gen_pass.grid(row=3, column=2)
add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(row=1, column=2)

window.mainloop()
