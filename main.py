from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
FONT_NAME = "Courier"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", bg=WHITE, font=(FONT_NAME, 12, "bold"))
website_text.grid(column=0, row=1)

#website_input = Text(height = 1, width = 35)
website_input = Entry(width = 35)
website_input.grid(column=1, row=1, columnspan =2)

email_text = Label(text="Email/Username:", bg=WHITE, font=(FONT_NAME, 12, "bold"))
email_text.grid(column=0, row=2)

#email_input = Text(height = 1, width = 35)
email_input = Entry(width = 35)
email_input.grid(column=1, row=2, columnspan =2)

password_text = Label(text="Password:", bg=WHITE, font=(FONT_NAME, 12, "bold"))
password_text.grid(column=0, row=3)

#password_input = Text(height = 1, width = 21)
password_input = Entry(width = 21)
password_input.grid(column=1, row=3)

password_button = Button(text="Generate Password", highlightthickness=0)
# password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width = 36)
add_button.grid(column=1, row=4, columnspan =2)



window.mainloop()