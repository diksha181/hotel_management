from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1295x550+230+220")

        #--------VARIABLES----------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_custName=StringVar()
        self.var_depName=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()

        #------TITLE-------------------------
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #--------LOGO-------------------
        img2=Image.open(r"C:\Users\DIKSHA PANDEY\OneDrive\Desktop\hotel_management_system\images\logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=100,height=40)

        #---------LABEL FRAME-----------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #-----------LABELS AND ENTRIES-----------
        #Customer Reference
        lbl_cust_ref=Label(labelframeleft,text="Customer Reference",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=25,font=("arial",12,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #Customer Name
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_custName,width=25,font=("arial",12,"bold"))
        txtcname.grid(row=1,column=1)

        #Dependent Name 
        dname=Label(labelframeleft,text="Dependent Name",font=("arial",12,"bold"),padx=2,pady=6)
        dname.grid(row=2,column=0,sticky=W)
        txtdname=ttk.Entry(labelframeleft,textvariable=self.var_depName,width=25,font=("arial",12,"bold"))
        txtdname.grid(row=2,column=1)

        #Gender
        gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=23,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=3,column=1)

        #Postcode
        lblpostcode=Label(labelframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtlblpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=25,font=("arial",12,"bold"))
        txtlblpostcode.grid(row=4,column=1)

        #Mobile Number 
        lblmobile=Label(labelframeleft,text="Mobile Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)
        txtlblmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=25,font=("arial",12,"bold"))
        txtlblmobile.grid(row=5,column=1)

        #Email
        lblemail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        txtlblemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=25,font=("arial",12,"bold"))
        txtlblemail.grid(row=6,column=1)

        #Nationality
        lblnation=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblnation.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=23,state="readonly")
        combo_nation["value"]=("Indian","American","Australian","British","Japanese")
        combo_nation.grid(row=7,column=1)
        
        #idproof
        lblid=Label(labelframeleft,text="ID Proof",font=("arial",12,"bold"),padx=2,pady=6)
        lblid.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=23,state="readonly")
        combo_id["value"]=("Aadhar Card","Passport","Drivers License","Voter ID Card","PAN Card")
        combo_id.grid(row=8,column=1)

        #idnumber
        lblidnumber=Label(labelframeleft,text="ID Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)
        txtlblidnumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=25,font=("arial",12,"bold"))
        txtlblidnumber.grid(row=9,column=1)

        #address
        lbladdress=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)
        txtlbladdress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=25,font=("arial",12,"bold"))
        txtlbladdress.grid(row=10,column=1)

        #-------Buttons--------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_info,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_info,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1)

        #-----------Table Frame Search System-----------
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=23,state="readonly")
        combo_search["value"]=("Refernce Number","Name","Mobile Number")
        combo_search.grid(row=0,column=1,padx=2)

        self.textSearch=StringVar()
        txtlblsearch=ttk.Entry(Table_Frame,textvariable=self.textSearch,width=23,font=("arial",12,"bold"))
        txtlblsearch.grid(row=0,column=2,padx=2)

        btn_search=Button(Table_Frame,text="Search",command=self.search_info,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=2)

        btn_ShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_ShowAll.grid(row=0,column=4,padx=2)

        #----------Details Frame------------
        details_frame=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL) 

        self.Cust_Details_Table=ttk.Treeview(details_frame,columns=("Ref","Name","Dep","Gender","Postal Code","Mobile Number","Email ID","Nationality","ID Proof","ID Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref",text="Refernce Number")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("Dep",text="Dependent Name")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("Postal Code",text="Postal Code")
        self.Cust_Details_Table.heading("Mobile Number",text="Mobile Number")
        self.Cust_Details_Table.heading("Email ID",text="Email ID")
        self.Cust_Details_Table.heading("Nationality",text="Nationality")
        self.Cust_Details_Table.heading("ID Proof",text="ID Proof")
        self.Cust_Details_Table.heading("ID Number",text="ID Number")
        self.Cust_Details_Table.heading("Address",text="Address")

        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("Dep",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Postal Code",width=100)
        self.Cust_Details_Table.column("Mobile Number",width=100)
        self.Cust_Details_Table.column("Email ID",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("ID Proof",width=100)
        self.Cust_Details_Table.column("ID Number",width=100)
        self.Cust_Details_Table.column("Address",width=100)

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_idproof.get()=="":
            messagebox.showerror("Error","Please fill all the details")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                self.var_custName.get(),
                                                                                                self.var_depName.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_idproof.get(),
                                                                                                self.var_idnumber.get(),
                                                                                                self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_custName.set(row[1]),
        self.var_depName.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute('update customer set Name=%s,Dependent=%s,Gender=%s,PostCode=%s,Mobile=%s,EmailID=%s,Nationality=%s,IDProof=%s,IDNumber=%s,Address=%s where Ref=%s',(self.var_custName.get(),
                           self.var_depName.get(),
                                    self.var_gender.get(),
                                    self.var_post.get(),
                                    self.var_mobile.get(),
                                    self.var_email.get(),
                                    self.var_nationality.get(),
                                    self.var_idproof.get(),
                                    self.var_idnumber.get(),
                                    self.var_address.get(),
                                    self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def delete_info(self):
        delete_info=messagebox.askyesno("Hotel Management System","Do you want to delete the data?",parent=self.root)
        if delete_info>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_info:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_info(self):
        self.var_ref.set(""),
        self.var_custName.set(""),
        self.var_depName.set(""),
        self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search_info(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.textSearch.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()