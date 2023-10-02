import tkinter as tk
from tkinter import messagebox

# Create an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and Phone fields are required.")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search for a contact
def search_contact():
    search_text = search_entry.get().lower()
    found_contacts = []

    for contact in contacts:
        if (search_text in contact["Name"].lower()) or (search_text in contact["Phone"]):
            found_contacts.append(contact)

    contact_listbox.delete(0, tk.END)
    if found_contacts:
        for contact in found_contacts:
            contact_listbox.insert(tk.END, contact["Name"] + " - " + contact["Phone"])
    else:
        contact_listbox.insert(tk.END, "No matching contacts found.")

# Function to view the selected contact's details
def view_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contact = contacts[index]
        messagebox.showinfo("Contact Details", f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
    else:
        messagebox.showwarning("Warning", "Please select a contact to view.")

# Function to update a contact's details
def update_selected_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contact = contacts[index]
        contact["Name"] = name_entry.get()
        contact["Phone"] = phone_entry.get()
        contact["Email"] = email_entry.get()
        contact["Address"] = address_entry.get()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update.")

# Function to delete a contact
def delete_selected_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        del contacts[index]
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

# Create the main window
app = tk.Tk()
app.title("Contact Management App")
app.geometry("600x400")
app.configure(bg="#CCE1F2")  # Set the background color to Azureish White

# Create and configure widgets
frame = tk.Frame(app, bg="#C6F8E5")  # Set the frame background color to Aero Blue
frame.pack(pady=20)

name_label = tk.Label(frame, text="Name:", bg="#C6F8E5")  # Set label background color to Aero Blue
name_label.grid(row=0, column=0, padx=10)

name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(frame, text="Phone:", bg="#C6F8E5")  # Set label background color to Aero Blue
phone_label.grid(row=1, column=0, padx=10)

phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(frame, text="Email:", bg="#C6F8E5")  # Set label background color to Aero Blue
email_label.grid(row=2, column=0, padx=10)

email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)

address_label = tk.Label(frame, text="Address:", bg="#C6F8E5")  # Set label background color to Aero Blue
address_label.grid(row=3, column=0, padx=10)

address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1)

add_button = tk.Button(frame, text="Add Contact", command=add_contact, bg="#FBF7D5", fg="#333333")  # Set button background and text color
add_button.grid(row=4, columnspan=2, pady=10)

search_label = tk.Label(frame, text="Search:", bg="#C6F8E5")  # Set label background color to Aero Blue
search_label.grid(row=5, column=0, padx=10)

search_entry = tk.Entry(frame, width=30)
search_entry.grid(row=5, column=1)

search_button = tk.Button(frame, text="Search", command=search_contact, bg="#FBF7D5", fg="#333333")  # Set button background and text color
search_button.grid(row=6, columnspan=2, pady=10)

contact_listbox = tk.Listbox(frame, width=50, height=10)
contact_listbox.grid(row=7, columnspan=2)

view_button = tk.Button(frame, text="View Contact", command=view_contact, bg="#F9DED7", fg="#333333")  # Set button background and text color
view_button.grid(row=8, column=0, padx=10, pady=10)

update_button = tk.Button(frame, text="Update Contact", command=update_selected_contact, bg="#F9DED7", fg="#333333")  # Set button background and text color
update_button.grid(row=8, column=1, pady=10)

delete_button = tk.Button(frame, text="Delete Contact", command=delete_selected_contact, bg="#F5CDDE", fg="#333333")  # Set button background and text color
delete_button.grid(row=9, columnspan=2, pady=10)

# Start the application main loop
app.mainloop()
