from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #--------1st image-------------------
        img1=Image.open(r"C:\Users\DIKSHA PANDEY\OneDrive\Desktop\hotel_management_system\images\logo.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #--------LOGO-------------------
        img2=Image.open(r"C:\Users\DIKSHA PANDEY\OneDrive\Desktop\hotel_management_system\images\logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=100,height=40)

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()