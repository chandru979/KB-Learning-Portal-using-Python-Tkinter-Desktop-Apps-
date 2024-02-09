from tkinter import*
import customtkinter 
import PIL.Image
from PIL import ImageTk
import tkinter as tk
import mysql.connector
from datetime import *
import time
from tkinter import messagebox,filedialog
from change_user_pass import *
import change_user_pass
from change_admin_pass import *
import change_admin_pass
from start import *

class Admin_page:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('Admin page')
        self.root.config(bg="white")
        Admin_page.admin_page(self)

    def admin_page(self):
            
        frame1=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="light blue")
        frame1.place(x=300,y=0,width=1300,height=60)

        title = customtkinter.CTkLabel(frame1,text='Admin Page',text_color='black',text_font=("Times new roman", 15, "bold"))
        title.place(x=550,y=10)

        x_button=customtkinter.CTkButton(frame1,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.root.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=1190,y=10)

        self.sideframe=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="light blue",bg_color="light blue")
        self.sideframe.place(x=0,y=0,width=300,height=1080)

        self.img = ImageTk.PhotoImage(PIL.Image.open("images\\logo_kb.png"))
        label = customtkinter.CTkLabel(self.sideframe, image = self.img)
        label.place(x=1,y=0,width=300,height=250)

        user_details_button=customtkinter.CTkButton(self.sideframe,command=self.manage_user,text='Manage User',text_font=("Times new roman", 15, "bold"),
                                                    text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        user_details_button.place(x=40,y=280)

        manage_course_details_button=customtkinter.CTkButton(self.sideframe,text='Manage Courses',text_font=("Times new roman", 15, "bold"),
                                                    text_color='black',command=self.manage_courses, fg_color="light blue",bg_color="light blue",width=5)
        manage_course_details_button.place(x=40,y=340)

        change_user_password_button=customtkinter.CTkButton(self.sideframe,command=self.chan_password,
                                                            text='Change User Password', fg_color="light blue",text_font=("Times new roman", 15, "bold"),text_color='black', bg_color="light blue",width=5)
        change_user_password_button.place(x=40,y=400)

        change_admin_password_button=customtkinter.CTkButton(self.sideframe,command=self.chan_admin_password,text='Change Admin Password',
                                                              fg_color="light blue",text_font=("Times new roman", 15, "bold"),text_color='black', bg_color="light blue",width=5)
        change_admin_password_button.place(x=40,y=460)

        feedback_report_button=customtkinter.CTkButton(self.sideframe,command=self.feedback_report, fg_color="light blue",text='Feedback Report',
                                                       text_font=("Times new roman", 15, "bold"),text_color='black', bg_color="light blue",width=5)
        feedback_report_button.place(x=40,y=520)

        logout_button=customtkinter.CTkButton(self.sideframe,text='Logout', fg_color="light blue",text_font=("Times new roman", 15, "bold"),
                                              text_color='black',command=self.logout, bg_color="light blue",width=5)
        logout_button.place(x=40,y=580)

        self.date_time = customtkinter.CTkLabel(self.sideframe)
        self.date_time.place(x=30,y=750,width=260)
        self.show_date()

    def manage_user(self):
        self.frame2=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="white")
        self.frame2.place(x=0,y=0,width=1920,height=1080)
        
        self.sideframe1=customtkinter.CTkFrame(self.frame2,relief=GROOVE,fg_color="light blue",bg_color="#FFFFFF")
        self.sideframe1.place(x=0,y=0,width=300,height=1080)

        self.img1 = ImageTk.PhotoImage(PIL.Image.open("images\\logo_kb.png"))
        label = customtkinter.CTkLabel(self.sideframe1, image = self.img1)
        label.place(x=1,y=0,width=300,height=250)

        user_details_button=customtkinter.CTkButton(self.sideframe1,command=self.user_details,text='User Details',text_font=("Times new roman", 15, "bold"),
                                                text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        user_details_button.place(x=40,y=280)

        add_user_button=customtkinter.CTkButton(self.sideframe1,command=self.add_user,text='Add User',text_font=("Times new roman", 15, "bold"),
                                                text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        add_user_button.place(x=40,y=340)

        edit_user_button=customtkinter.CTkButton(self.sideframe1,text='Edit User',text_font=("Times new roman", 15, "bold"),text_color='black', 
                                                 command=self.edit_user,bg_color="light blue",fg_color="light blue",width=5)
        edit_user_button.place(x=40,y=400)

        delete_user_button=customtkinter.CTkButton(self.sideframe1,text='Delete User',command=self.delete_user,text_font=("Times new roman", 15, "bold"),
                                                   text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        delete_user_button.place(x=40,y=460)

        exit_button=customtkinter.CTkButton(self.sideframe1,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='black',
                                            command= self.frame2.destroy, fg_color="light blue",bg_color="light blue",width=5)
        exit_button.place(x=40,y=520)

    def manage_courses(self):

        self.frame4=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="white")
        self.frame4.place(x=0,y=0,width=1920,height=1080)
        
        self.sideframe2=customtkinter.CTkFrame(self.frame4,relief=GROOVE,fg_color="light blue",bg_color="#FFFFFF")
        self.sideframe2.place(x=0,y=0,width=300,height=1080)

        self.img1 = ImageTk.PhotoImage(PIL.Image.open("images\\logo_kb.png"))
        label1 = customtkinter.CTkLabel(self.sideframe2, image = self.img1)
        label1.place(x=1,y=0,width=300,height=250)

        course_details_button=customtkinter.CTkButton(self.sideframe2,text='Course Details',text_font=("Times new roman", 15, "bold"),
                                                text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        course_details_button.place(x=40,y=280)

        add_course_button=customtkinter.CTkButton(self.sideframe2,text='Add course',text_font=("Times new roman", 15, "bold"),
                                                text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        add_course_button.place(x=40,y=340)

        delete_course_button=customtkinter.CTkButton(self.sideframe2,text='Delete course',command=self.delete_user,text_font=("Times new roman", 15, "bold"),
                                                   text_color='black', fg_color="light blue",bg_color="light blue",width=5)
        delete_course_button.place(x=40,y=400)

        exit_button=customtkinter.CTkButton(self.sideframe2,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='black',
                                            command= self.frame4.destroy, fg_color="light blue",bg_color="light blue",width=5)
        exit_button.place(x=40,y=460)

    def feedback_report(self):

        self.frame6=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame6.place(x=300, y=0, width=1300, height=1080)

        self.feedback_Label = customtkinter.CTkLabel(self.frame6, text="Feedback Report",text_font=("Times new roman",15, "bold"),bg_color="orange",fg_color="orange",text_color="black")
        self.feedback_Label.place(x=400, y=10)

        x_button=customtkinter.CTkButton(self.frame6,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame6.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=560,y=10,height=30)

        report_button = customtkinter.CTkButton(self.frame6,text="Report",command=self.feedback_report_details ,text_font=("Times new roman",15),
                                                                                                bg_color="#263238",fg_color="black",text_color="white")
        report_button.place(x=10,y=100)

        self.details_Label = customtkinter.CTkLabel(self.frame6, text="User_ID                   User_Feedback",
                                                    text_font=("Times new roman",15, "bold"),bg_color="#263238",fg_color="#263238",text_color="white")
        self.details_Label.place(x=100, y=150)

    def feedback_report_details(self):

        self.frame10=customtkinter.CTkFrame(self.frame6,relief=GROOVE,fg_color="light blue",bg_color="light blue")
        self.frame10.place(x=50, y=190, width=1000, height=600)

        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("select u_id,f_feedback from feedback")
        i=0 
        for feedback in my_cursor: 
            for j in range(len(feedback)):
                feedback_Entry = Entry(self.frame10,width=30)
                feedback_Entry.grid(row=i, column=j,pady=10,padx=5,ipadx=5,ipady=5) 
                feedback_Entry.insert(END, feedback[j])
            i=i+1
        connection.close()
        
    def user_details(self):
        self.frame7=customtkinter.CTkFrame(self.frame2,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame7.place(x=300, y=0, width=1300, height=1080)

        self.user_details_Label = customtkinter.CTkLabel(self.frame7, text="User Details",text_font=("Times new roman",15, "bold"),bg_color="orange",fg_color="orange",text_color="black")
        self.user_details_Label.place(x=450, y=10)

        x_button=customtkinter.CTkButton(self.frame7,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame7.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=590,y=10,height=30)

        self.frame8=customtkinter.CTkFrame(self.frame7,relief=GROOVE,fg_color="light blue",bg_color="light blue")
        self.frame8.place(x=50, y=80, width=1000, height=700)

        self.details_Label = customtkinter.CTkLabel(self.frame7, text="        User_ID              User_Name            User_Password        User_Gmail            User_Domain         User_Phone_no",text_font=("Times new roman",15, "bold"),bg_color="#263238",fg_color="#263238",text_color="white")
        self.details_Label.place(x=50, y=50)

        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("select * from user")
        i=0 
        for user in my_cursor: 
            for j in range(len(user)):
                userdetails_Entry = Entry(self.frame8,width=20, fg='black')
                userdetails_Entry.grid(row=i, column=j,pady=10,padx=20,ipady=5) 
                userdetails_Entry.insert(END, user[j])
            i=i+1
        connection.close()

       

    def add_user(self):
        
        self.frame3=customtkinter.CTkFrame(self.frame2,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame3.place(x=300, y=0, width=1300, height=1080)

        self.adduser_Label = customtkinter.CTkLabel(self.frame3, text="Add User Details",text_font=("Times new roman",15, "bold"),bg_color="orange",fg_color="orange",text_color="black")
        self.adduser_Label.place(x=400, y=10)

        x_button=customtkinter.CTkButton(self.frame3,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame3.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=560,y=10,height=30)

        self.userid_Label = customtkinter.CTkLabel(self.frame3, text="User ID:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.userid_Label.place(x=100, y=280)
        self.userid_Entry = customtkinter.CTkEntry(self.frame3,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.userid_Entry.place(x=300, y=280)  

        self.username_Label = customtkinter.CTkLabel(self.frame3, text="User Name:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.username_Label.place(x=100, y=340)
        self.username_Entry = customtkinter.CTkEntry(self.frame3,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.username_Entry.place(x=300, y=340)  
        
        self.password_Label = customtkinter.CTkLabel(self.frame3,text="Password:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.password_Label.place(x=100, y=400)  
        self.password_Entry = customtkinter.CTkEntry(self.frame3,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.password_Entry.place(x=300, y=400)
        
        self.email_Label = customtkinter.CTkLabel(self.frame3,text="Email ID:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.email_Label.place(x=100, y=460)  
        self.email_Entry = customtkinter.CTkEntry(self.frame3,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.email_Entry.place(x=300, y=460)

        self.domain_Label = customtkinter.CTkLabel(self.frame3,text="Domain:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.domain_Label.place(x=100, y=220)  
        self.domain_Entry = customtkinter.CTkEntry(self.frame3,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.domain_Entry.place(x=300, y=220)

        self.phone_no_Label = customtkinter.CTkLabel(self.frame3,text="Phone no:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.phone_no_Label.place(x=100, y=520)  
        self.phone_no_Entry = customtkinter.CTkEntry(self.frame3,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.phone_no_Entry.place(x=300, y=520)
        
        clear_button = customtkinter.CTkButton(self.frame3,text="CLEAR",text_font=("Times new roman",15),command=self.clear_text,bg_color="#263238",fg_color="black",text_color="white")
        clear_button.place(x=100,y=580)
        
        ok_button = customtkinter.CTkButton(self.frame3,text="OK",command=lambda: self.add_user_details(self.userid_Entry.get(),self.username_Entry.get(),self.password_Entry.get(),self.email_Entry.get(),self.domain_Entry.get(),
                                                                                                self.phone_no_Entry.get()) ,text_font=("Times new roman",15),
                                                                                                bg_color="#263238",fg_color="black",text_color="white")
        ok_button.place(x=300,y=580)
    
    def add_user_details(self,id,name,password,email,domain,phone_no):
        
        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("insert into user values (%s,%s,%s,%s,%s,%s)",(id,name,password,email,domain,phone_no))
        # messagebox.showinfo("SUCCESS","Successfully added")
        connection.commit()
        connection.close()

    def edit_user(self):

        self.frame9=customtkinter.CTkFrame(self.frame2,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame9.place(x=300, y=0, width=1300, height=1080)

        self.update_user_Label = customtkinter.CTkLabel(self.frame9, text="Update User Details",text_font=("Times new roman",15, "bold"),bg_color="orange",fg_color="orange",text_color="black")
        self.update_user_Label.place(x=400, y=10)
        

        x_button=customtkinter.CTkButton(self.frame9,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame9.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=580,y=10,height=30)
       
        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("select * from user")
        my_cursor.fetchall()
       
        self.userid1_Label = customtkinter.CTkLabel(self.frame9, text="User ID:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.userid1_Label.place(x=100, y=280)
        self.userid1_Entry = customtkinter.CTkEntry(self.frame9,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.userid1_Entry.place(x=300, y=280)  

        self.username1_Label = customtkinter.CTkLabel(self.frame9, text="User Name:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.username1_Label.place(x=100, y=340)
        self.username1_Entry = customtkinter.CTkEntry(self.frame9,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.username1_Entry.place(x=300, y=340)  
        
        self.password1_Label = customtkinter.CTkLabel(self.frame9,text="Password:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.password1_Label.place(x=100, y=400)  
        self.password1_Entry = customtkinter.CTkEntry(self.frame9,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.password1_Entry.place(x=300, y=400)
        
        self.email1_Label = customtkinter.CTkLabel(self.frame9,text="Email ID:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.email1_Label.place(x=100, y=460)  
        self.email1_Entry = customtkinter.CTkEntry(self.frame9,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.email1_Entry.place(x=300, y=460)

        self.domain1_Label = customtkinter.CTkLabel(self.frame9,text="Domain:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.domain1_Label.place(x=100, y=220)  
        self.domain1_Entry = customtkinter.CTkEntry(self.frame9,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.domain1_Entry.place(x=300, y=220)

        self.phone_no1_Label = customtkinter.CTkLabel(self.frame9,text="Phone no:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.phone_no1_Label.place(x=100, y=520)  
        self.phone_no1_Entry = customtkinter.CTkEntry(self.frame9,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.phone_no1_Entry.place(x=300, y=520)

        self.update_button = customtkinter.CTkButton(self.frame9,text="Update",command=lambda: self.update_user(self.userid1_Entry.get(),self.username1_Entry.get(),
                                                                                    self.password1_Entry.get(),self.email1_Entry.get(),self.domain1_Entry.get(),
                                                                                    self.phone_no1_Entry.get()) ,text_font=("Times new roman",15),
                                                                            bg_color="#263238",fg_color="black",text_color="white")
        self.update_button.place(x=200,y=580)

       
    def update_user(self,u_id,u_username,u_password,u_email,domain,phone_no):
          
        conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal',port='3306')

        my_cursor = conn.cursor()
        my_cursor.execute("update user set u_id=%s,u_username=%s,u_password=%s,u_email=%s,domain=%s,phone_no=%s where u_id=%s",
                          (u_id,u_username,u_password,u_email,domain,phone_no,u_id))
    
        # messagebox.showinfo("Success", "Details updated Successfully")
        conn.commit()
        conn.close()

    def delete_user(self):

        self.frame5=customtkinter.CTkFrame(self.frame2,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame5.place(x=300, y=0, width=1300, height=1080)

        self.deleteuser_Label = customtkinter.CTkLabel(self.frame5, text="Delete User Details",text_font=("Times new roman",15, "bold"),bg_color="orange",fg_color="orange",text_color="black")
        self.deleteuser_Label.place(x=400, y=10)

        x_button=customtkinter.CTkButton(self.frame5,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame5.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=580,y=10,height=30)

        self.userid_delete_Label = customtkinter.CTkLabel(self.frame5, text="User ID:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",text_color="white")
        self.userid_delete_Label.place(x=100, y=280)
        self.userid_delete_Entry = customtkinter.CTkEntry(self.frame5,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.userid_delete_Entry.place(x=300, y=280) 
   
        ok_button = customtkinter.CTkButton(self.frame5,text="OK",command=lambda: self.delete_user_details(self.userid_delete_Entry.get()),
                                            text_font=("Times new roman",15),bg_color="#263238",fg_color="black",text_color="white")
        ok_button.place(x=500,y=280)

    def delete_user_details(self,id):
        if id == id:
            connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
            my_cursor = connection.cursor()
            delete = "delete from user where u_id= %s"
            self.id=[(id)]
            my_cursor.execute(delete,self.id)
            connection.commit()
            connection.close()
        #     messagebox.showinfo("SUCCESS","Successfully deleted")
        # else:
        #     messagebox.showerror("FAILED","Please enter user ID")


    def clear_text(self):

        self.userid_Entry.delete(0, END)
        self.username_Entry.delete(0, END)
        self.password_Entry.delete(0, END)
        self.domain_Entry.delete(0, END)
        self.phone_no_Entry.delete(0, END)
        self.email_Entry.delete(0, END)

    def show_date(self):

        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%Y:%m:%d")

        set_text = f"Time: {self.time} \nDate: {self.date}"
        self.date_time.configure(text=set_text,font=("Times new roman",14),text_color="black",bg_color="light blue")
        self.date_time.after(100,self.show_date)

    
    def chan_password(self):
        change = change_password(self.root)
    
    def chan_admin_password(self):
        change1 = change_admin_password(self.root)
        
    def logout(self):
        messagebox.showinfo("SUCCESS","Successfully logout")
        log = login_design(self.root)


if __name__ == '__main__':
    root=Tk()
    obj=Admin_page(root)
    root.mainloop()