import tkinter as tk
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    password_length = int(length_var.get())
    if password_length < 4:
        password_length = 4

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_var.set(password)

def copy_password():
    password = password_var.get()
    if password:
        pyperclip.copy(password)

# Create the main window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")
app.configure(bg="#333333")  # Dark Gray background

# Create and configure widgets
frame = tk.Frame(app, bg="#333333")  # Dark Gray background
frame.pack(pady=20)

label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12), bg="#333333", fg="white")  # White text
label.grid(row=0, column=0, padx=10)

length_var = tk.StringVar()
length_var.set(12)  # Default password length
entry = tk.Entry(frame, textvar=length_var, font=("Helvetica", 12))
entry.grid(row=0, column=1)

generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 12), command=generate_password, bg="#444444", fg="white")  # Darker background
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_var = tk.StringVar()
password_label = tk.Label(frame, textvar=password_var, font=("Helvetica", 12), bg="#333333", fg="white")  # White text
password_label.grid(row=2, column=0, columnspan=2)

copy_button = tk.Button(frame, text="Copy Password", font=("Helvetica", 12), command=copy_password, bg="#444444", fg="white")  # Darker background
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the application main loop
app.mainloop()
