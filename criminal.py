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
        self.root.title('CENTRAL BUREAU OF INVESTIGATION')
        
        

        #VARIABLES

        #Criminal Table variables
        self.var_criminal_id = StringVar()
        self.var_criminal_name = StringVar()
        self.var_address = StringVar()
        self.var_aadhar_no = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_occupation = StringVar()
        self.var_gender = StringVar()

        #FIR table variables
        self.var_fir_no = StringVar()
        #self.var_criminal_name = StringVar() (foreign key)
        self.var_date_of_crime = StringVar()
        self.var_date_of_arrest = StringVar()
        self.var_aliase = StringVar()
        self.var_crime_type = StringVar()
        self.var_wanted = StringVar()

        
        
        



        #creating the heading label
        lbl_title = Label(self.root, text = ' CENTRAL BUREAU OF INVESTIGATION',font=('times new roman',40,'bold'),bg='black',fg='white')
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
        #1.criminal id
        criminal_id =  Label(upper_frame, text = 'Criminal ID:',font=('arial',11,'bold'),bg='white')
        criminal_id.grid(row=0, column=0, padx = 2,sticky = W)
        entry1_id = ttk.Entry(upper_frame, textvariable=self.var_criminal_id, width = 22,font=('arial',11,'bold') )
        entry1_id.grid(row=0, column = 1, padx = 2, sticky = W)
        
        #2-criminal_name
        criminal_name = Label(upper_frame, text = ' Name of the Criminal:',font=('arial',11,'bold'),bg='white')
        criminal_name.grid(row=0, column=2, padx = 2,pady =7,sticky = W)
        entry2_id = ttk.Entry(upper_frame,textvariable=self.var_criminal_name, width = 22,font=('arial',11,'bold') )
        entry2_id.grid(row=0, column = 3, padx = 2,pady = 7)
   
        #3-address
        address=  Label(upper_frame, text = ' Address:',font=('arial',11,'bold'),bg='white')
        address.grid(row=0, column=4, padx = 2,pady =7,sticky = W)
        entry3_id = ttk.Entry(upper_frame,textvariable=self.var_address, width = 22,font=('arial',11,'bold') )
        entry3_id.grid(row=0, column = 5, padx = 2,pady = 7, sticky = W)

        #4-aadhar_no
        aadhar_no=  Label(upper_frame, text = ' Aadhar No:',font=('arial',11,'bold'),bg='white')
        aadhar_no.grid(row=0, column=6, padx = 2,pady =7,sticky = W)
        entry4_id = ttk.Entry(upper_frame,textvariable=self.var_aadhar_no, width = 22,font=('arial',11,'bold') )
        entry4_id.grid(row=0, column = 7, padx = 2,pady = 7, sticky = W)

        #5-date_of_crime
        date_of_birth=  Label(upper_frame, text = ' Date of Birth:',font=('arial',11,'bold'),bg='white')
        date_of_birth.grid(row=0, column=8, padx = 2,pady =7,sticky = W)
        entry5_id = ttk.Entry(upper_frame,textvariable=self.var_date_of_birth, width = 22,font=('arial',11,'bold') )
        entry5_id.grid(row=0, column = 9, padx = 2,pady = 7, sticky = W)

        #6-occupation
        occupation=  Label(upper_frame, text = ' Occupation:',font=('arial',11,'bold'),bg='white')
        occupation.grid(row=1, column=0, padx = 2,pady =7,sticky = W)
        entry6_id = ttk.Entry(upper_frame,textvariable=self.var_occupation, width = 22,font=('arial',11,'bold') )
        entry6_id.grid(row=1, column = 1, padx = 2,pady = 7, sticky = W)

        #7-FIR No
        fir_no=  Label(upper_frame, text = 'FIR No:',font=('arial',11,'bold'),bg='white')
        fir_no.grid(row=1, column=2, padx = 2,pady =7,sticky = W)
        entry7_id = ttk.Entry(upper_frame,textvariable=self.var_fir_no, width = 22,font=('arial',11,'bold') )
        entry7_id.grid(row=1, column = 3, padx = 2,pady = 7, sticky = W)

        #8-date_of_crime
        date_of_crime=  Label(upper_frame, text = ' Date of Crime:',font=('arial',11,'bold'),bg='white')
        date_of_crime.grid(row=1, column=4, padx = 2,pady =7,sticky = W)
        entry8_id = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width = 22,font=('arial',11,'bold') )
        entry8_id.grid(row=1, column = 5, padx = 2,pady = 7, sticky = W)

        #9-date_of_arrest
        date_of_arrest=  Label(upper_frame, text = ' Date of Arrest:',font=('arial',11,'bold'),bg='white')
        date_of_arrest.grid(row=1, column=6, padx = 2,pady =7,sticky = W)
        entry9_id = ttk.Entry(upper_frame,textvariable=self.var_date_of_arrest, width = 22,font=('arial',11,'bold') )
        entry9_id.grid(row=1, column = 7, padx = 2,pady = 7, sticky = W)

        #10-aliase
        aliase = Label(upper_frame, text = ' Aliase:',font=('arial',11,'bold'),bg='white')
        aliase.grid(row=1, column=8, padx = 2,pady =7,sticky = W)
        entry10_id = ttk.Entry(upper_frame,textvariable=self.var_aliase, width = 22,font=('arial',11,'bold') )
        entry10_id.grid(row=1, column = 9, padx = 2,pady = 7, sticky = W)

        
        #11-gender
        gender=  Label(upper_frame, text = 'Gender:',font=('arial',11,'bold'),bg='white')
        gender.grid(row=2, column=0, padx = 2,pady =7,sticky = W)

        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=85,y=78,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=("arial",9,"bold"),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)  

        #12-wanted
        wanted = Label(upper_frame, text = ' Most Wanted:',font=('arial',11,'bold'),bg='white')
        wanted.grid(row=2, column=2, padx = 2,pady =7,sticky = W)
        
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=435,y=78,width=190,height=30)
        
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=("arial",9,"bold"),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='no',value='no',font=("arial",9,"bold"),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #13-crime_type
        crime_type=  Label(upper_frame, text = ' Crime Type:',font=('arial',11,'bold'),bg='white')
        crime_type.grid(row=2, column=6, padx = 2,pady =7,sticky = W)
        entry11_id = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width = 22,font=('arial',11,'bold') )
        entry11_id.grid(row=2, column = 7, padx = 2,pady = 7, sticky = W)

       

        #button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        #add button
        btn_add=Button(button_frame,command = self.add_data, text='Save Record',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
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
        combo_search_box['value']=('Select Option','CriminalId') #have to add FIRNo later when i figure out the search function
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

        self.criminal_table = ttk.Treeview(table_frame, column=('1','2','3','4','5','6','7','8','9','10','11','12','13'),xscrollcommand = scroll_x.set, yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command= self.criminal_table.xview)
        scroll_y.config(command= self.criminal_table.yview)


        self.criminal_table.heading('1',text='Criminal Id')
        self.criminal_table.heading('2',text='Name of the criminal')
        self.criminal_table.heading('3',text='Address')
        self.criminal_table.heading('4',text='Aadhar No')
        self.criminal_table.heading('5',text='Date of Birth')
        self.criminal_table.heading('6',text='Occupation')
        self.criminal_table.heading('7',text='FIR No')
        self.criminal_table.heading('8',text='Date of Crime')
        self.criminal_table.heading('9',text='Date of Arrest')
        self.criminal_table.heading('10',text='Aliase')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Gender')
        self.criminal_table.heading('13',text='Most Wanted')
        

        self.criminal_table['show']='headings'


        #To change the width of the columns in the table 
        """self.criminal_table.column('1', width=50)
        self.criminal_table.column('2', width=120)
        self.criminal_table.column('3', width=300)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=70)
        self.criminal_table.column('6', width=90)
        self.criminal_table.column('7', width=70)
        self.criminal_table.column('8', width=70)
        self.criminal_table.column('9', width=70)
        self.criminal_table.column('10', width=50)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=50)
        self.criminal_table.column('13', width=70)"""





        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        #self.fetch_data()

        


    #ADD FUNCTION
    def add_data(self):
        if self.var_criminal_id.get() == "":
            messagebox.showerror('Error','All Fields are required', parent = self.root)

        else:
            try:
                conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='CriminalRecord')
                mycursor = conn.cursor()

                mycursor.execute('insert into Criminal values(%s,%s,%s,%s,%s,%s,%s)',(
                        self.var_criminal_id.get(),
                        self.var_criminal_name.get(),
                        self.var_address.get(),
                        self.var_aadhar_no.get(),
                        self.var_date_of_birth.get(),
                        self.var_occupation.get(),
                        self.var_gender.get()
                ))

                mycursor.execute('insert into FIR values(%s,%s,%s,%s,%s,%s,%s)',(
                        self.var_fir_no.get(),
                        self.var_criminal_id.get(),
                        self.var_date_of_crime.get(),
                        self.var_date_of_arrest.get(),
                        self.var_aliase.get(),
                        self.var_crime_type.get(),
                        self.var_wanted.get()
                ))




                conn.commit()
                self.fetch_data()
                #self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')





    #fetch Data
                
    def fetch_data(self):
        conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='CriminalRecord')
        my_cursor=conn.cursor()
        
        my_cursor.execute('select distinct(c.CriminalId), c.name, c.address, c.aadhar_no, c.date_of_birth, c.occupation,f.FIRNo,f.date_of_crime, f.date_of_arrest, f.aliase, f.crime_type, c.gender, f.wanted from Criminal c, FIR f where c.CriminalId = f.CriminalNo;')
        data=my_cursor.fetchall()

        print(data)
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

        self.var_criminal_id.set(data[0])
        self.var_criminal_name.set(data[1])
        self.var_address.set(data[2])
        self.var_aadhar_no.set(data[3])
        self.var_date_of_birth.set(data[4])
        self.var_occupation.set(data[5])
        self.var_fir_no.set(data[6])
        self.var_date_of_crime.set(data[7])
        self.var_date_of_arrest.set(data[8])
        self.var_aliase.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_gender.set(data[11])
        self.var_wanted.set(data[12])
        

    #UPDATE
    def update_data(self):
        if self.var_criminal_id.get() == "":
            messagebox.showerror('Error','All Fields are required', parent = self.root)

        else:
            try:
                update=messagebox.askyesno('Update','Are you sure?\n NOTE: Cannot update Criminal ID and FIR No' )
                if update>0:
                    conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='CriminalRecord')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update Criminal set name = %s,address=%s,aadhar_no = %s, date_of_birth = %s, occupation = %s, gender = %s where criminalId = %s',(self.var_criminal_name.get(),self.var_address.get(),self.var_aadhar_no.get(),self.var_date_of_birth.get(),self.var_occupation.get(),self.var_gender.get(),self.var_criminal_id.get()))

                    my_cursor.execute('update FIR set CriminalNo = %s,date_of_crime=%s,date_of_arrest = %s, aliase = %s, crime_type = %s, wanted = %s where FIRNo = %s',(
                        self.var_criminal_id.get(),
                        self.var_date_of_crime.get(),
                        self.var_date_of_arrest.get(),
                        self.var_aliase.get(),
                        self.var_crime_type.get(),
                        self.var_wanted.get(),
                        self.var_fir_no.get())) 


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
        if self.var_criminal_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete= messagebox.askyesno('Delete','Are you sure you want to delete the record?')
                if Delete>0:
                    conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='CriminalRecord')
                    my_cursor = conn.cursor()
                    sql = 'delete from Criminal where CriminalId = %s'
                    value = (self.var_criminal_id.get(),)
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
        self.var_criminal_id.set("")
        self.var_criminal_name.set("")
        self.var_address.set("")
        self.var_aadhar_no.set("")
        self.var_date_of_birth.set("")
        self.var_occupation.set("")
        self.var_fir_no.set("")
        self.var_date_of_crime.set("")
        self.var_date_of_arrest.set("")
        self.var_aliase.set("")
        self.var_crime_type.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn= mysql.connector.connect(host='crms-database.c1cu4w0w6899.ap-southeast-2.rds.amazonaws.com',username='admin',password='crms2024', database='CriminalRecord')
                my_cursor=conn.cursor()
                my_cursor.execute('select distinct(c.CriminalId), c.name, c.address, c.aadhar_no, c.date_of_birth, c.occupation,f.FIRNo,f.date_of_crime, f.date_of_arrest, f.aliase, f.crime_type, c.gender, f.wanted from Criminal c, FIR f where c.CriminalId = f.CriminalNo AND ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("", END, values=i)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}')  
    def test(self):
        pass

if __name__ == "__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
    
