from tkinter import*
import customtkinter 
import tkinter as tk
import mysql.connector
from tkinter import messagebox

class change_password():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('change password')
        change_password.forgot_pass(self)
        
    def forgot_pass(self):

        frame1=customtkinter.CTkFrame(self.root,relief=GROOVE,bg_color='black',fg_color='#263238')
        frame1.place(x=0, y=0, width=1920, height=1080)


        forgot_label = customtkinter.CTkLabel(frame1, text="Forgot/Change Password", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="#263238", fg_color="orange",width=419)
        forgot_label.place(x=550, y=10)
        x_button=customtkinter.CTkButton(frame1,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=frame1.destroy,bg_color="black", fg_color="black",width=5)
        x_button.place(x=950,y=10)

        mail_label = customtkinter.CTkLabel(frame1, text="Email Id",text_font=("Times new roman", 15, "bold"),text_color='white',bg_color="#263238",fg_color="#263238",width=90)
        mail_label.place(x=40, y=70)
        mail_entry =customtkinter.CTkEntry(frame1, width=300,height=20,text_font=("Times new roman", 15),text_color='white',border_width=0,fg_color='black',cursor="hand2")
        mail_entry.place(x=55, y=100)

        verify_pass = customtkinter.CTkButton(frame1, text="verify", command=lambda: self.verify(mail_entry.get()),text_font=("Times new roman", 15, "bold"), fg_color="black",
                                            text_color="#fa333e", cursor="hand2")
        verify_pass.place(x=370, y=100)

        self.new_pass_label = customtkinter.CTkLabel(frame1, text="New Password", text_font=("Times new roman", 15, "bold"),
                                    text_color='white', bg_color="#263238", fg_color="#263238", width=90)

        self.new_pass_entry = customtkinter.CTkEntry(frame1, width=300, height=20, text_font=("Times new roman", 15),
                                                text_color='white', border_width=0, fg_color='black', show='*',
                                                cursor="hand2")

        self.confirm_pass_label = customtkinter.CTkLabel(frame1, text="Confirm Password", text_font=("Times new roman", 15, "bold"),
                                                text_color='white', bg_color="#263238", fg_color="#263238", width=90)

        self.confirm_pass_entry = customtkinter.CTkEntry(frame1, width=300, height=20, text_font=("Times new roman", 15),
                                                    text_color='white', border_width=0, fg_color='black', show='*',
                                                    cursor="hand2")

        self.reset_button = customtkinter.CTkButton(frame1, text='Reset',command=lambda: self.changepassword(mail_entry.get(),self.new_pass_entry.get(),self.confirm_pass_entry.get()), text_font=("Times new roman", 15, "bold"),
                                                text_color='orange', bg_color="#263238", fg_color="black", width=1,
                                                cursor="hand2")
        
    def verify(self,email):
        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='kbportal',port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("select count(*) from user where u_email=%s", (email,))
        row = my_cursor.fetchone()
        connection.close()
        if(row[0]==1):
            self.new_pass_label.place(x=50, y=130)
            self.new_pass_entry.place(x=55, y=160)
            self.confirm_pass_label.place(x=50, y=190)
            self.confirm_pass_entry.place(x=55, y=220)
            self.reset_button.place(x=280, y=250)
            
    def changepassword(self,email,password,confirm_password):

        if(password == confirm_password):
            connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
            my_cursor = connection.cursor()
            my_cursor.execute("update user set u_password=%s where u_email=%s", (password,email))
            connection.commit()
            connection.close()
            messagebox.showinfo("SUCCESS","Successfully updated")
        else:
            messagebox.showinfo("ERROR","New Password and Confirm Password is not matched")


if __name__ == '__main__':
    root=Tk()
    obj=change_password(root)
    root.mainloop()