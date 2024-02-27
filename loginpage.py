from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import criminal

class Login:
    def __init__(self, root):

    


        # Create the main window
        self.root = root#tk.Tk()
        self.root.title("CRIMINAL RECORDS SYSTEM MANAGEMENT-Login")
        self.root.geometry("1270x700")

        #adding image file
        bg_image = Image.open('images\cyberlogin.jpg')
        bg = ImageTk.PhotoImage(bg_image)

        #creating the background canvas
        canvas1 = Canvas(self.root, width = 1270, height = 700)
        canvas1.pack(fill = "both", expand = True)

        #Display the image in the background
        canvas1.create_image(0,0,image = bg,anchor=CENTER)

        canvas1.create_text(630, 200, text="Welcome", fill = "white",font=('times new roman',20,'bold'))

        self.var_username= StringVar()
        self.var_password = StringVar()

# Load the image
#image = Image.open("images/ice_bear.jpg")
#photo = ImageTk.PhotoImage(image)

# Create a label for the image
#image_label = tk.Label(root, image=photo)
#image_label.pack()

#Label Heading
#login_label = Label(root, text = 'LOGIN TO ENTER',font=('times new roman',20,'bold'),fg='white')
#login_label.place(x=20, y=20, width = 500, height=50)

    # Create a frame in the middle
        middle_frame = Frame(self.root, bg="black", bd = 2,  relief=RIDGE)
        middle_frame.place(x = 500, y = 300, width = 270, height =150 )

    # Username Label and Entry
        username_label = Label(middle_frame, text="  Username :",font=('arial',11,'bold'),bg='black', fg = "white")
        username_label.grid(row=1, column=0, padx = 10, pady = 10, sticky="w")
        username_entry = Entry(middle_frame, textvariable=self.var_username)
        username_entry.grid(row=1, column=1, padx = 5, pady = 5)

    # Password Label and Entry
        password_label = Label(middle_frame, text="  Password :",font=('arial',11,'bold'),bg='black', fg = "white")
        password_label.grid(row=2, column=0,padx = 10, pady = 5, sticky="w")
        password_entry = Entry(middle_frame, show="*", textvariable=self.var_password)
        password_entry.grid(row=2, padx = 5, pady = 5,column=1)

    # Frame for the login button
        button_frame = Frame(middle_frame)
        button_frame.place(x=100, y = 90, width = 70, height = 25)

    # Login Button
        login_button = Button(button_frame, text="Login", command=self.validate_login , width = 14,font=('arial',11,'bold'),bg='gray', fg = "white")
        login_button.pack()


    def validate_login(self):
        if self.var_username.get() == "" or self.var_password.get() == "":
                messagebox.showerror('Error','All Fields are required', parent = self.root)

        else:
            try:
                conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',   password='crms2024', database='CriminalRecord')
                my_cursor = conn.cursor()
                my_cursor.execute('select username,password from Login where usertype = "admin"')
                username_data = my_cursor.fetchall()
                print(username_data)
                for i in username_data:
                    if self.var_username.get() == i[0] and self.var_password.get() == i[1]:
                        print("Worked")
                        criminal.Criminal(self.root)
                        messagebox.showinfo('Success',"Login Successful!")
                        break
                    else:
                        messagebox.showinfo('Fail to Login','Incorrect username or password')
                        
                     
                     
    # Dummy validation - You should replace this with actual authentication logic
    #if username == "admin" and password == "password":
        # If login successful, show a message box
        #messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    #else:
        # If login failed, show an error message box
        #messagebox.showerror("Login Failed", "Invalid username or password")
            
            except Exception as es:
                    messagebox.showerror('Error',f'Due to {str(es)}')  




# Run the Tkinter main loop
if __name__ == "__main__": 
    root=Tk()
    obj=Login(root)
    root.mainloop()
