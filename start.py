from tkinter import*
import customtkinter 
import PIL.Image
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox

class login_design:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('LOGIN PAGE')
        login_design.design(self)

    def design(self):

        self.frame1=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="light blue",bg_color="#FFFFFF")
        self.frame1.pack()
        self.frame1.place(x=0, y=0, width=1920, height=1080)
        self.img1 = ImageTk.PhotoImage(PIL.Image.open("images\\login_back.jpg"))
        self.label1 = Label(self.frame1, image = self.img1).place(x=0,y=200,width=1920,height=800)

        frame2=customtkinter.CTkFrame(relief=GROOVE,fg_color="light blue",bg_color="#FFFFFF")
        frame2.place(x=0, y=0, width=1920, height=200)
        
        self.img2 = ImageTk.PhotoImage(PIL.Image.open("images\\logo_kb.png"))
        self.label2 = Label(frame2, image = self.img2).place(x=0,y=0,width=200,height=200)
        title = customtkinter.CTkLabel(frame2,text="KNOWLEDGE BASE LEARNING PORTAL",text_font=("Times new roman",20,"bold"),width=40,bg_color="light blue",
                                       text_color="black")
        title.place(x=400, y=65)
        # x_button=customtkinter.CTkButton(self.root,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.root.destroy,bg_color="#263238", fg_color="#263238",width=5)
        # x_button.place(x=1500,y=10)
    
        self.login_label=customtkinter.CTkLabel(self.frame1,text="LOGIN",text_font=("Times new roman",17,"bold"),bg_color="light blue",text_color="black").place(x=610,y=270)
        
        global username,access
        username = StringVar()
        username_Label = customtkinter.CTkLabel(self.frame1, text="User Name",text_font=("Times new roman",15),bg_color="light blue",fg_color="light blue",text_color="black").place(x=555, y=320)
        username_Entry = customtkinter.CTkEntry(self.frame1,text=username,text_font=("Times new roman",15),bg_color="light blue",fg_color="#FFFFFF",text_color="black").place(x=710, y=320)  

        access  = StringVar()
        enter = customtkinter.CTkLabel(self.frame1,text="Password",text_font=("Times new roman",15),bg_color="light blue",fg_color="light blue",text_color="black").place(x=555, y=370)  
        enter_ent = customtkinter.CTkEntry(self.frame1,text=access,show='*',text_font=("Times new roman",15),bg_color="light blue",fg_color="#FFFFFF",text_color="black").place(x=710, y=370)

        show_password_Button = customtkinter.CTkButton(self.frame1, text="*",text_font=("Times new roman",15),fg_color="light blue",bg_color="light blue",command=self.show_password,text_color="black",cursor="hand2")
        show_password_Button.place(x=855, y=375,width=30,height=20) 

        login_Button = customtkinter.CTkButton(self.frame1, text="Login now",text_font=("Times new roman",15),bg_color="blue",fg_color="blue",command=self.Login,text_color="white",cursor="hand2")
        login_Button.place(x=560, y=420) 

        admin_user = customtkinter.CTkButton(self.frame1,text="Admin",command=self.admin_page,text_color='white',bg_color="blue",fg_color="blue",text_font=("Times new roman", 15),cursor="hand2")
        admin_user.place(x=710,y=420)
        
        fgt_pass=customtkinter.CTkButton(self.frame1,text="Forgot password ?",text_font=("Times new roman", 15),bg_color="light blue",fg_color="light blue",command=self.chan_password,text_color="black",cursor="hand2")
        fgt_pass.place(x=555,y=470)
  
    def admin_page(self):
        from admin_login import Admin
        admin = Admin(self.root)

    def show_password(self):
        global password_1
        password_1 = access.get()
        customtkinter.CTkLabel(self.frame1,text="Your Password: "+str(password_1)).place(x=890,y=370)

    def chan_password(self):
        from change_user_pass import change_password
        change = change_password(self.root)
      
    def Login(self):

        if username.get() == "" or access.get() == "":
            messagebox.showerror("Error","Fill all the field")
        else:
            connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='kbportal',port='3306')
            my_cursor=connection.cursor()
            my_cursor.execute("select count(*) from user where u_username=%s and u_password=%s",(username.get() ,access.get()))
            row=my_cursor.fetchone()
            connection.close()
            if row==0:
                messagebox.showerror("Error","Invalid username or password")
            elif row[0]==1:
                messagebox.showinfo("Welcome", "Welcome to KB Portal")
                self.new_window = Toplevel()
                from home_page import home
                self.root = home(self.new_window)

if __name__ == '__main__':
    root=Tk()
    obj=login_design(root)
    root.mainloop()