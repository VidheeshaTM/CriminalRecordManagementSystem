from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox



class Criminal:
    def __init__(self, root):
        self.root = root

        #creating the window
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')


        #VARIABLES
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_criminal_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()



        #creating the heading label
        lbl_title = Label(self.root, text = ' CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='white')
        lbl_title.place(x=0, y=0, width = 1530, height=70)

        #logo
        img_logo = Image.open('images/policelogo1.jpg')
        img_logo= img_logo.resize((60,60),Image.LANCZOS)  
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image = self.photo_logo)
        self.logo.place(x=70, y = 5, width = 60, height = 60)

        
        #criminal tape frame frame
        criminialtape_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'white')
        criminialtape_frame.place(x=0, y=70, width = 1530, height=50)


        #images police
        """
        img_logo = Image.open('images/backgroundimgcrp1.jpg')
        img_logo= img_logo.resize((1530,230),Image.LANCZOS)  
        self.photo_background=ImageTk.PhotoImage(img_logo)

        self.backgrd = Label(self.root, image = self.photo_background)
        self.backgrd.place(x=0, y = 70, width = 1530, height = 230)
        """

        #MAIN FRAME
        main_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'white')
        main_frame.place(x=0, y=120, width = 1530, height=660) 

        #Criminal record
        #1
        upper_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, bg = 'white',text = 'Criminal Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=5, y=5, width = 1515, height=325) 

        #LABEL ENTRIES
        #case_id
        case_id =  Label(upper_frame, text = 'Case ID',font=('arial',11,'bold'),bg='white')
        case_id.grid(row=0, column=0, padx = 2,sticky = W)
        entry1_id = ttk.Entry(upper_frame, textvariable=self.var_case_id, width = 22,font=('arial',11,'bold') )
        entry1_id.grid(row=0, column = 1, padx = 2, sticky = W)
        
        #criminal_no
        criminal_no=  Label(upper_frame, text = 'Criminal ID',font=('arial',11,'bold'),bg='white')
        criminal_no.grid(row=0, column=2, padx = 2,pady =7,sticky = W)
        entry2_id = ttk.Entry(upper_frame,textvariable=self.var_criminal_no, width = 22,font=('arial',11,'bold') )
        entry2_id.grid(row=0, column = 3, padx = 2,pady = 7)
   
        #criminal_name
        criminal_name=  Label(upper_frame, text = 'Criminal Name',font=('arial',11,'bold'),bg='white')
        criminal_name.grid(row=1, column=0, padx = 2,pady =7,sticky = W)
        entry3_id = ttk.Entry(upper_frame,textvariable=self.var_criminal_name, width = 22,font=('arial',11,'bold') )
        entry3_id.grid(row=1, column = 1, padx = 2,pady = 7, sticky = W)

        #arrest date
        arrest_date=  Label(upper_frame, text = 'Arrest Date',font=('arial',11,'bold'),bg='white')
        arrest_date.grid(row=1, column=2, padx = 2,pady =7,sticky = W)
        entry4_id = ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width = 22,font=('arial',11,'bold') )
        entry4_id.grid(row=1, column = 3, padx = 2,pady = 7, sticky = W)

        #date of crime
        dateof_crime=  Label(upper_frame, text = 'Date of crime',font=('arial',11,'bold'),bg='white')
        dateof_crime.grid(row=2, column=0, padx = 2,pady =7,sticky = W)
        entry5_id = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width = 22,font=('arial',11,'bold') )
        entry5_id.grid(row=2, column = 1, padx = 2,pady = 7, sticky = W)

        #address
        address=  Label(upper_frame, text = 'Address:',font=('arial',11,'bold'),bg='white')
        address.grid(row=2, column=2, padx = 2,pady =7,sticky = W)
        entry6_id = ttk.Entry(upper_frame, textvariable=self.var_address,width = 22,font=('arial',11,'bold') )
        entry6_id.grid(row=2, column = 3, padx = 2,pady = 7, sticky = W)
        
        #age
        age=  Label(upper_frame, text = 'Age',font=('arial',11,'bold'),bg='white')
        age.grid(row=3, column=0, padx = 2,pady =7,sticky = W)
        entry7_id = ttk.Entry(upper_frame,textvariable=self.var_age, width = 22,font=('arial',11,'bold') )
        entry7_id.grid(row=3, column = 1, padx = 2,pady = 7, sticky = W)

        #occupation
        occupation=  Label(upper_frame, text = 'occupation',font=('arial',11,'bold'),bg='white')
        occupation.grid(row=3, column=2, padx = 2,pady =7,sticky = W)
        entry8_id = ttk.Entry(upper_frame, textvariable=self.var_occupation,width = 22,font=('arial',11,'bold') )
        entry8_id.grid(row=3, column = 3, padx = 2,pady = 7, sticky = W)

        #crime type
        crime_type=  Label(upper_frame, text = 'Crime Type',font=('arial',11,'bold'),bg='white')
        crime_type.grid(row=4, column=0, padx = 2,pady =7,sticky = W)
        entry9_id = ttk.Entry(upper_frame, textvariable=self.var_crime_type,width = 22,font=('arial',11,'bold') )
        entry9_id.grid(row=4, column = 1, padx = 2,pady = 7, sticky = W)

        #father name
        father_name=  Label(upper_frame, text = 'Father Name',font=('arial',11,'bold'),bg='white')
        father_name.grid(row=4, column=2, padx = 2,pady =7,sticky = W)
        entry2_id = ttk.Entry(upper_frame, textvariable=self.var_father_name,width = 22,font=('arial',11,'bold') )
        entry2_id.grid(row=4, column = 3, padx = 2,pady = 7, sticky = W)
        
        #gender
        gender=  Label(upper_frame, text = 'Gender',font=('arial',11,'bold'),bg='white')
        gender.grid(row=0, column=4, padx = 2,pady =7,sticky = W)
        
        #wanted
        wanted=  Label(upper_frame, text = 'Most Wanted',font=('arial',11,'bold'),bg='white')
        wanted.grid(row=1, column=4, padx = 2,pady =7,sticky = W)
        
        #radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=5,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=("arial",9,"bold"),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
        #radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=730,y=45,width=190,height=30)
        
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=("arial",9,"bold"),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='no',value='no',font=("arial",9,"bold"),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        #add button
        btn_add=Button(button_frame,command = self.add_data, text='Record Save',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #update button
        btn_update=Button(button_frame, command = self.update_data,text='Update',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete button
        btn_delete=Button(button_frame,command = self.delete_data,text='Delete',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear button
        btn_clear=Button(button_frame,command = self.clear_data, text='Clear',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)



        #2
        lower_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, bg = 'white',text = 'Criminal Information Table',font=('times new roman',11,'bold'),fg='red')
        lower_frame.place(x=5, y=340, width = 1515, height=325) 

        #2-1
        search_frame = LabelFrame(lower_frame, bd = 2, relief = RIDGE, bg = 'white',text = 'Search Criminal Record',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=5, y=5, width = 1505, height=70) 


        #label2
        search_by= Label(search_frame, text = 'Search By',font=('arial',11,'bold'),bg="red",fg="white")
        search_by.grid(row=0, column=0, padx = 5,sticky = W)

        self.var_com_search= StringVar()
        combo_search_box=ttk.Combobox(search_frame, textvariable = self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_Id','Criminal_No')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)


        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable = self.var_search,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)


        #search button
        btn_search=Button(search_frame,command = self.search_data,text='Search',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,sticky=W,padx=5)

        #all button
        btn_all=Button(search_frame,command = self.fetch_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)


        #TABLE FRAME
        table_frame = Frame(lower_frame, bd=2, relief = RIDGE)
        table_frame.place(x = 5, y = 65, width = 1505, height = 170)


        

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand = scroll_x.set, yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command= self.criminal_table.xview)
        scroll_y.config(command= self.criminal_table.yview)


        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CriminalNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestName')
        self.criminal_table.heading('6',text='DateOfCrime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'


        #To change the width of the colums in the table 
        self.criminal_table.column('1', width=100)



        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #ADD FUNCTION
    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error','All Fields are required', parent = self.root)

        else:
            try:
                conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='learndb')
                mycursor = conn.cursor()

                mycursor.execute('insert into criminalbase values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        self.var_case_id.get(),
                        self.var_criminal_no.get(),
                        self.var_criminal_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthmark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get()


                ))

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')





    #fetch Data
                
    def fetch_data(self):
        conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='learndb')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminalbase')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    #get cursor
        
    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_criminal_name.set(data[2])
        self.var_criminal_name.set(data[3])
        self.var_nickname.set(data[4])
        self.var_arrest_date.set(data[5])
        self.var_date_of_crime.set(data[6])
        self.var_address.set(data[7])
        self.var_age.set(data[8])
        self.var_occupation.set(data[9])
        self.var_birthmark.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    #UPDATE
    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error','All Fields are required', parent = self.root)

        else:
            try:
                update=messagebox.askyesno('Update','Are you sure?' )
                if update>0:
                    conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='learndb')
                    my_cursor=conn.cursor()
                    #my_cursor.execute('update criminalbase set Criminal_No=%s, criminal_Name = %s'........................ blah blah blah all attributes,(self.var_criminal_id.get(), etc etc))
                else:
                    if not update:
                        return
                    
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record successfully updated')

            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')


    #DELETE
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete= messagebox.askyesno('Delete','Are you sure you want to delete the record?')
                if Delete>0:
                    conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='learndb')
                    my_cursor = conn.cursor()
                    sql = 'delete from criminalbase where case_id = %s'
                    value = (self.var_case_id.get(),)
                    my_cursor.execute(sql,value)

                else:
                    if not Delete:
                        return
                    
                conn.commit()

                self.fetch_data()
                self.clear_data()
                conn.close()
        
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')


    #CLEAR
                
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_criminal_name.set("")
        self.var_criminal_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='learndb')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminalbase where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("", END, values=i)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')


















if __name__ == "__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()