from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Details_Room:
    def __init__(self,root):
        self.root=root
        self.root.title("Details")
        self.root.geometry("1295x550+230+220")

        #---------VARIABLES----------------
        self.var_floor=StringVar()
        self.var_room_no=StringVar()
        self.var_room_type=StringVar()

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
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Adding a New Room',font=("times new roman",13,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=520,height=350)

        #-----------LABELS AND ENTRIES-----------
        #Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=25,font=("arial",12,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No
        room_no=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        room_no.grid(row=1,column=0,sticky=W)
        txtroom_no=ttk.Entry(labelframeleft,textvariable=self.var_room_no,width=25,font=("arial",12,"bold"))
        txtroom_no.grid(row=1,column=1)

        #Room Type 
        roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        roomtype.grid(row=3,column=0,sticky=W)

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_room_type,font=("arial",12,"bold"),width=23,state="readonly")
        combo_roomtype["value"]=("Studio","Deluxe","Presidential","Single","Double","Suite")
        combo_roomtype.grid(row=3,column=1)

        #-----------BUTTONS------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_info,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_info,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1)

        #-----------Table Frame Search System-----------
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details',font=("times new roman",13,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL) 
        self.room_table=ttk.Treeview(Table_Frame,columns=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("RoomNo",text="Room No")
        self.room_table.heading("RoomType",text="Room Type")
        

        self.room_table.column("Floor",width=100)
        self.room_table.column("RoomNo",width=100)
        self.room_table.column("RoomType",width=100)
        

        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #--------ADD DATA-----------
    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error","Please fill all the details")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),
                                                                       self.var_room_no.get(),
                                                                       self.var_room_type.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New room has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #-------------FETCH DATA---------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2]),

    #--------UPDATE DATA------------
    def update(self):
        if self.var_room_no.get()=="":
            messagebox.showerror("Error","Please enter the room number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute('update details set floor=%s,room_type=%s where room_no=%s',(self.var_floor.get(),
                                                                                            self.var_room_type.get(),
                                                                                            self.var_room_no.get()))
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
            query="delete from details where room_no=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_info:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    #-----------RESET DATA-------------
    def reset_info(self):
        self.var_floor.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set(""),
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Details_Room(root)
    root.mainloop()