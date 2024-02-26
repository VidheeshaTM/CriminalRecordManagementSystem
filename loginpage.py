import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Dummy validation - You should replace this with actual authentication logic
    if username == "admin" and password == "password":
        # If login successful, show a message box
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        # If login failed, show an error message box
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("CRIMINAL RECORDS SYSTEM MANAGEMENT-Login")

# Load the image
image = Image.open("images/ice_bear.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label for the image
image_label = tk.Label(root, image=photo)
image_label.pack()

# Create a frame in the middle
middle_frame = tk.Frame(root)
middle_frame.pack(pady=20)

# Username Label and Entry
username_label = tk.Label(middle_frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(middle_frame)
username_entry.grid(row=0, column=1)

# Password Label and Entry
password_label = tk.Label(middle_frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(middle_frame, show="*")
password_entry.grid(row=1, column=1)

# Frame for the login button
button_frame = tk.Frame(middle_frame)
button_frame.grid(row=2, columnspan=2)

# Login Button
login_button = tk.Button(button_frame, text="Login", command=validate_login)
login_button.pack()

# Run the Tkinter main loop
root.mainloop()
