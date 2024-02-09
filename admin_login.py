from tkinter import*
import customtkinter 
import tkinter as tk
import mysql.connector
from datetime import *
import time
from tkinter import messagebox
from admin_page import *
import admin_page
from start import *
import start

class Admin:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('Admin Page')

        self.frame=customtkinter.CTkFrame(self.root,relief=GROOVE,bg_color='black',fg_color='#263238')
        self.frame.place(x=0, y=0, width=1920, height=1080)
        Admin.admin_login_page(self)
        

    def admin_login_page(self):
        
        admin_label = customtkinter.CTkLabel(self.frame, text="Admin Login Page", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="#263238", fg_color="orange",width=419)
        admin_label.place(x=550, y=10)

        self.frame1=customtkinter.CTkFrame(relief=GROOVE,fg_color="light blue",bg_color="light blue")
        self.frame1.place(x=500, y=250, width=500, height=250)

        x_button=customtkinter.CTkButton(self.frame,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.root.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=1500,y=10)
        
        self.adminlogin_Label = customtkinter.CTkLabel(self.frame1, text="Admin Login",text_font=("Times new roman",15,"bold"),bg_color="light blue",
                                                       fg_color="light blue",text_color="black")
        self.adminlogin_Label.place(x=160, y=20)

        self.login_label=customtkinter.CTkLabel(self.frame1,text="LOGIN",text_font=("Times new roman",17,"bold"),bg_color="#263238",text_color="white").place(x=610,y=270)
    
        self.adminname_Label = customtkinter.CTkLabel(self.frame1, text="Admin Name",text_font=("Times new roman",15),bg_color="light blue",
                                                      fg_color="light blue",text_color="black")
        self.adminname_Label.place(x=80, y=70)
        self.adminname_Entry = customtkinter.CTkEntry(self.frame1,text_font=("Times new roman",15),bg_color="light blue",fg_color="#FFFFFF",text_color="black")
        self.adminname_Entry.place(x=250, y=70)  
        
        self.adminpassword = StringVar()
        self.adminpassword_Label = customtkinter.CTkLabel(self.frame1,text="Password",text_font=("Times new roman",15),bg_color="light blue",fg_color="light blue",
                                                          text_color="black")
        self.adminpassword_Label.place(x=80, y=110)  
        self.adminpassword_Entry = customtkinter.CTkEntry(self.frame1,text=self.adminpassword,show='*',text_font=("Times new roman",15),bg_color="light blue",fg_color="#FFFFFF",text_color="black")
        self.adminpassword_Entry.place(x=250, y=110)

        self.show_password_Button = customtkinter.CTkButton(self.frame1, text="*",text_font=("Times new roman",15),
                                                            bg_color="light blue",fg_color="light blue",command=self.show_password,text_color="black",cursor="hand2")
        self.show_password_Button.place(x=400, y=115,width=30,height=20) 

        self.admin_login_Button = customtkinter.CTkButton(self.frame1, text="Login",text_font=("Times new roman",15,"bold"),bg_color="blue",fg_color="blue",
                                                          command=self.admin_login,text_color="#FFFFFF",cursor="hand2")
        self.admin_login_Button.place(x=80, y=180) 

        self.user_login_Button = customtkinter.CTkButton(self.frame1, text="User Login",text_font=("Times new roman",15,"bold"),bg_color="blue",fg_color="blue",
                                                         command=self.user_login,text_color="#FFFFFF",cursor="hand2")
        self.user_login_Button.place(x=250, y=180) 

        self.admin_forgot_pass_Button = customtkinter.CTkButton(self.frame1,command=self.chan_admin_password ,text="Forgot Password ?",
                                                                text_font=("Times new roman",15),bg_color="light blue",fg_color="light blue",text_color="black",cursor="hand2")
        self.admin_forgot_pass_Button.place(x=80, y=220) 

    def user_login(self):
        from start import login_design
        log = login_design(self.root)

    def chan_admin_password(self):
        from change_admin_pass import change_admin_password
        change1 = change_admin_password(self.root)

    def show_password(self):
        password_1 = self.adminpassword.get()
        customtkinter.CTkLabel(self.frame1,text="Password: "+str(password_1)).place(x=200,y=140)


    def admin_login(self):
        if self.adminname_Entry.get() == "" or self.adminpassword_Entry.get() == "":
            messagebox.showerror("Error","Fill all the field")
        else:
            connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='kbportal',port='3306')
            my_cursor=connection.cursor()
            my_cursor.execute("select count(*) from admin where admin_name=%s and admin_password=%s",(
                self.adminname_Entry.get(),
                self.adminpassword_Entry.get()
            ))
            row=my_cursor.fetchone()
            connection.close()
            if row==0:
                messagebox.showerror("Error","Invalid username or password")
            elif row[0]==1:
                messagebox.showinfo("Welcome", "Welcome to Admin Page")
                self.new_window = Toplevel()
                self.root = Admin_page(self.new_window)

    
if __name__ == '__main__':
    root=Tk()
    obj=Admin(root)
    root.mainloop()