from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = "Times New Roman", 10, "bold"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    if len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Make sure ypu haven't left any fields empty")
    else:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details that you have entered: \nEmail:{email}"
                                               f"\nPassword: {password} \n Is it ok to save")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website}|{email}|{password}\n")
                web_input.delete(0, END)
                email_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
# label
web_label = Label(text="Website:", font=FONT_NAME)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=FONT_NAME)
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:", font=FONT_NAME)
pass_label.grid(column=0, row=3)

# entry
web_input = Entry(width=35, )
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

# button
pass_button = Button(text="Generate Password", font=FONT_NAME, command=generate)
pass_button.grid(column=3, row=3)

add_button = Button(text="Add", font=FONT_NAME, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)

canvas.grid(column=1, row=0)
window.mainloop()
