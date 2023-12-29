from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Room_Book:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1295x550+230+220")

        #---------VARIABLES----------------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_duration=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #------TITLE-------------------------
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #--------LOGO-------------------
        img2=Image.open(r"C:\Users\DIKSHA PANDEY\OneDrive\Desktop\hotel_management_system\images\logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=100,height=40)

        #---------LABEL FRAME-----------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Details',font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #-----------LABELS AND ENTRIES-----------
        #Customer Reference
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #Fetch Data button
        btn_fetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btn_fetchData.place(x=343,y=4)

        #Check in date
        check_in_date=Label(labelframeleft,text="Check In Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=25,font=("arial",12,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #Check out date
        check_out_date=Label(labelframeleft,text="Check Out Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=25,font=("arial",12,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        #Room Type 
        roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select room_type from details")
        ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=23,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.grid(row=3,column=1)

        #Available Room
        lblAvailRoom=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
        lblAvailRoom.grid(row=4,column=0,sticky=W)
        # txtlblAvailRoom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=25,font=("arial",12,"bold"))
        # txtlblAvailRoom.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select room_no from details")
        rows=my_cursor.fetchall()

        combo_room_no=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=23,state="readonly")
        combo_room_no["value"]=rows
        combo_room_no.grid(row=4,column=1)

        #Meal 
        lblmeal=Label(labelframeleft,text="Meal Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)
        txtlblmeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=25,font=("arial",12,"bold"))
        txtlblmeal.grid(row=5,column=1)

        #Duration of stay 
        lblduration=Label(labelframeleft,text="Duration",font=("arial",12,"bold"),padx=2,pady=6)
        lblduration.grid(row=6,column=0,sticky=W)
        txtlblduration=ttk.Entry(labelframeleft,textvariable=self.var_duration,width=25,font=("arial",12,"bold"))
        txtlblduration.grid(row=6,column=1)

        #Paid tax
        lbltax=Label(labelframeleft,text="Payable Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lbltax.grid(row=7,column=0,sticky=W)
        txtlbltax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=25,font=("arial",12,"bold"))
        txtlbltax.grid(row=7,column=1)

        #Subtotal 
        lblSubTotal=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtlblSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=25,font=("arial",12,"bold"))
        txtlblSubTotal.grid(row=8,column=1)

        #Total
        lbltotal=Label(labelframeleft,text="Total",font=("arial",12,"bold"),padx=2,pady=6)
        lbltotal.grid(row=9,column=0,sticky=W)
        txtlbltotal=ttk.Entry(labelframeleft,textvariable=self.var_total,width=25,font=("arial",12,"bold"))
        txtlbltotal.grid(row=9,column=1)

        #Bill Button
        btn_bill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)

        #-----------BUTTONS------------------
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

        #--------------Right Side Image---------------
        img3=Image.open(r"C:\Users\DIKSHA PANDEY\OneDrive\Desktop\hotel_management_system\images\bed.jpeg")
        img3=img3.resize((520,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg3=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg3.place(x=760,y=55,width=520,height=300)

        #-----------Table Frame Search System-----------
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=23,state="readonly")
        combo_search["value"]=("Contact","Room")
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
        details_frame.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL) 
        self.room_table=ttk.Treeview(details_frame,columns=("Contact","CheckIn","CheckOut","RoomType","RoomAvailability","Meal","Duration"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("CheckIn",text="Check-In")
        self.room_table.heading("CheckOut",text="Check-Out")
        self.room_table.heading("RoomType",text="Room Type")
        self.room_table.heading("RoomAvailability",text="Room No")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("Duration",text="Duration")

        self.room_table.column("Contact",width=100)
        self.room_table.column("CheckIn",width=100)
        self.room_table.column("CheckOut",width=100)
        self.room_table.column("RoomType",width=100)
        self.room_table.column("RoomAvailability",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("Duration",width=100)

        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #----------FETCHING ALL DATA------------------
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror('Error','Please enter a contact number',parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Contact not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Ref from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Ref ID:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Name from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=30)
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblName.place(x=0,y=60)
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)

                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select EmailID from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Email ID:",font=("arial",12,"bold"))
                lblName.place(x=0,y=90)
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)

                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lblName.place(x=0,y=120)
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)

                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lblName.place(x=0,y=150)
                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=150)

    #--------ADD DATA-----------
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Please fill all the details")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_duration.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has been booked, Enjoy your stay :)",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #-------------FETCH DATA---------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #----------GET CURSOR-------------
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_duration.set(row[6]),
        
    #--------UPDATE DATA------------
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute('update room set check_in=%s,check_out=%s,room_type=%s,room_available=%s,meal=%s,duration=%s where Contact=%s',(self.var_checkin.get(),
             self.var_checkout.get(),
             self.var_roomtype.get(),
             self.var_roomavailable.get(),
             self.var_meal.get(),
             self.var_duration.get(),
             self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    #---------DELETE DATA--------------
    def delete_info(self):
        delete_info=messagebox.askyesno("Hotel Management System","Do you want to delete the data?",parent=self.root)
        if delete_info>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_info:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    #-----------RESET DATA-------------
    def reset_info(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_duration.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    #---------CALCULATE TOTAL-------------
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_duration.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Suite"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_duration.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(100)
            q2=float(400)
            q3=float(self.var_duration.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Studio"):
            q1=float(100)
            q2=float(300)
            q3=float(self.var_duration.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

    def search_info(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.textSearch.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=Room_Book(root)
    root.mainloop()