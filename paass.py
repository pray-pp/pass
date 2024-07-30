import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for length!")
        return
    
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    if not (include_upper or include_lower or include_digits or include_special):
        messagebox.showwarning("Input Error", "Select at least one character type!")
        return

    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

def on_enter(event):
    event.widget.config(relief="sunken")  # Sunken relief on hover

def on_leave(event):
    event.widget.config(relief="raised")  # Raised relief when not hovered

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x500")
root.config(bg="#1C1C1C")

length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12), bg="#1C1C1C", fg="#EDEDED")
length_label.pack(pady=10)

length_var = tk.StringVar(value="12")
length_entry = tk.Entry(root, textvar=length_var, font=("Helvetica", 12), width=10, bg="#EDEDED", fg="black", relief="sunken")
length_entry.pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", font=("Helvetica", 12), variable=upper_var, bg="#1C1C1C", fg="#EDEDED", selectcolor="#1C1C1C")
upper_check.pack(pady=5)

lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", font=("Helvetica", 12), variable=lower_var, bg="#1C1C1C", fg="#EDEDED", selectcolor="#1C1C1C")
lower_check.pack(pady=5)

digits_check = tk.Checkbutton(root, text="Include Digits", font=("Helvetica", 12), variable=digits_var, bg="#1C1C1C", fg="#EDEDED", selectcolor="#1C1C1C")
digits_check.pack(pady=5)

special_check = tk.Checkbutton(root, text="Include Special Characters", font=("Helvetica", 12), variable=special_var, bg="#1C1C1C", fg="#EDEDED", selectcolor="#1C1C1C")
special_check.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), command=generate_password, bg="#6C757D", fg="white", relief="raised", borderwidth=2, padx=10, pady=5)
generate_button.pack(pady=20)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12, "bold"), command=copy_to_clipboard, bg="#6C757D", fg="white", relief="raised", borderwidth=2, padx=10, pady=5)
copy_button.pack(pady=5)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvar=password_var, font=("Helvetica", 12), width=25, bg="#EDEDED", fg="black", relief="sunken", borderwidth=2)
password_entry.pack(pady=20)

root.mainloop()
