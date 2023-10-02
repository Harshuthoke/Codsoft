import tkinter as tk

# Function to update the display
def update_display(text):
    display_var.set(text)

# Function to handle button clicks
def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(display_var.get())
            update_display(result)
        except Exception as e:
            update_display("Error")
    elif text == "C":
        update_display("")
    else:
        current_text = display_var.get()
        current_text += text
        update_display(current_text)

# Create the main window
app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")
app.configure(bg="#f0f0f0")

# Create and configure the display
display_var = tk.StringVar()
display_var.set("")
display = tk.Entry(app, textvar=display_var, font=("Helvetica", 24), justify="right", bd=10, relief="sunken")
display.pack(fill="both", padx=10, pady=10, expand=True)

# Create and configure the buttons
button_frame = tk.Frame(app, bg="#f0f0f0")
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 18), width=5, height=2, bg="#dcdcdc")
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights to make buttons expandable
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Start the application main loop
app.mainloop()
