from tkinter import *
from tkinter import messagebox
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for cha in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")


# ------------------------CALL UP DETAILS-----------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("json.data", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            details = data[website]
            messagebox.showinfo(title=f"{website}", message=details)
        else:
            messagebox.showinfo(title="Error", message=f'There is no details for {website}')


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email, "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="You can not leave any field empty")
    else:
        feedback = messagebox.askokcancel(title=f"{website}",
                                          message=f"Email:{email}\n Password:{password}\n Is it okay?")

        if feedback:
            # reading the data_file
            try:
                with open("json.data", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("json.data", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                # update data_file
            else:
                data.update(new_data)
                # save the updated data_file
                with open("json.data", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "stdave001@gmail")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, columnspan=1)

# BUTTONS
gen_password = Button(text="Generate Password", width=15, command=generate_password)
gen_password.grid(column=3, row=3, columnspan=1)
add = Button(text="Add", width=30, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", command=find_password)
search.grid(column=3, row=1)

window.mainloop()
