from tkinter import*
import PIL.Image
from PIL import ImageTk
from datetime import *
import time
import customtkinter
import mysql.connector
from tkinter import messagebox,filedialog
import os
from tkinter.filedialog import askopenfile
from PyPDF2 import PdfReader
from tkVideoPlayer import TkinterVideo
import boto3

class home:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('Home page')        

        self.id = StringVar()
        self.name = StringVar()
        self.domain = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.phone = StringVar()

        sideframe=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="light blue",bg_color="light blue")
        sideframe.place(x=0,y=0,width=300,height=1080)

        self.frame1=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="sky blue",bg_color="sky blue")
        self.frame1.place(x=300,y=0,width=1300,height=60)

        
        logout_button = customtkinter.CTkButton( self.frame1, text='logout',text_color="white", fg_color='blue',
                                                text_font=('Times new roman',15),command=self.logout,cursor='hand2')
        logout_button.place(x=1050,y=10)
        self.img = ImageTk.PhotoImage(PIL.Image.open("images\\logo_kb.png"))
        label = customtkinter.CTkLabel(sideframe, image = self.img)
        label.place(x=1,y=0,width=300,height=250)

        self.frame4=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="sky blue",bg_color="#263238")
        self.frame4.place(x=300, y=40, width=1300, height=1080)

        self.content_label = customtkinter.CTkLabel(self.frame4,text=" Who we are\n"
"Aspire Systems is a global technology services firm serving as a trusted technology partner for our customers. \n We work with some of the worlds most innovative enterprises "
"and independent software vendors, helping them leverage technology and \noutsourcing in our specific areas of expertise.Our services include Product Engineering,"
 "Enterprise Solutions, Independent Testing \nServices and IT Infrastructure Support services. Our core philosophy of Attention. Always." 
"communicates our belief in \nlavishing care and attention on our customers and employees",text_font=("Times new roman",15),fg_color="sky blue",
                                               text_color="black",bg_color="sky blue")
        self.content_label.place(x=20, y=400) 

        self.img1 = ImageTk.PhotoImage(PIL.Image.open("images\\homepage_bg.jpg"))
        label = customtkinter.CTkLabel(self.frame4, image = self.img1)
        label.place(x=150,y=20)


        self.addframe = customtkinter.CTkFrame(self.frame4,relief=GROOVE,fg_color="white",bg_color="white")
        self.addframe.place(x=0,y=600,width=1300,height=150)

        self.address = customtkinter.CTkLabel(self.addframe,text="Address:",text_font=("Times new roman",15,"bold"),fg_color="white",
                                               text_color="black",bg_color="white")
        self.address.place(x=20, y=10) 

        
        self.address1 = customtkinter.CTkLabel(self.addframe,text="Social Media:",text_font=("Times new roman",15,"bold"),fg_color="white",
                                               text_color="black",bg_color="white")
        self.address1.place(x=300, y=10) 
    
        dashboard_label=customtkinter.CTkLabel(self.frame1,text="Dashboard",text_font=("Times new roman",15,"bold"),fg_color="sky blue",
                                               text_color="black",bg_color="sky blue")
        dashboard_label.place(x=500, y=10) 

        myprofile_button = customtkinter.CTkButton(sideframe, text="MyProfile", text_font=('Times new roman',15,"bold"),command=self.Myprofile,cursor='hand2',
                                                   bg_color="light blue",fg_color='light blue')
        myprofile_button.place(x=10,y=260,width=260)

        mycourse_button = customtkinter.CTkButton(sideframe, text="MyCourse", text_font=('Times new roman',15,"bold"),fg_color='light blue',command=self.Mycourse,cursor='hand2',bg_color="light blue")
        mycourse_button.place(x=10,y=320,width=260)

        feedback_button = customtkinter.CTkButton(sideframe, text="Feedback", text_font=('Times new roman',15,"bold"),fg_color='light blue',command=self.Feedback,cursor='hand2',bg_color="light blue")
        feedback_button.place(x=10,y=380,width=260)

        private_file_button = customtkinter.CTkButton(sideframe, text="Private File", text_font=('Times new roman',15,"bold"),fg_color='light blue',
                                                      command=self.user_privatefile_verify,cursor='hand2',bg_color="light blue")
        private_file_button.place(x=10,y=440,width=260)

        self.date_time = customtkinter.CTkLabel(sideframe)
        self.date_time.place(x=30,y=750,width=260)
        self.show_date()

    def show_date(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%Y:%m:%d")

        set_text = f"Time: {self.time} \nDate: {self.date}"
        self.date_time.configure(text=set_text,font=("Times new roman",14),text_color="black",bg_color="light blue")
        self.date_time.after(100,self.show_date)

    def logout(self):
        messagebox.showinfo("SUCCESS","Successfully logout")
        import start
        start.login_design(self.root)
    
    def Myprofile(self):

        self.frame2=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame2.place(x=300, y=0, width=1300, height=1080)

        self.frame3=customtkinter.CTkFrame(self.frame2,relief=GROOVE,fg_color="light blue",bg_color="light blue")
        self.frame3.place(x=0,y=0,width=1300,height=60)

        verify_label=customtkinter.CTkLabel(self.frame2,text="Verify",text_font=("Times new roman",15,"bold"),fg_color="light blue",
                                               text_color="black",bg_color="light blue")
        verify_label.place(x=400, y=10) 

        x_button=customtkinter.CTkButton(self.frame2,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame2.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=7)

        self.access  = StringVar()
        password_Label = customtkinter.CTkLabel(self.frame2,text="Password:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",
                                                text_color="white").place(x=20, y=100)  
        password_Entry = customtkinter.CTkEntry(self.frame2,text=self.access,show='*',text_font=("Times new roman",15),bg_color="#263238",fg_color="white",
                                                text_color="black").place(x=180, y=100)

        ok_Button = customtkinter.CTkButton(self.frame2, text="Ok",text_font=("Times new roman",15),bg_color="black",fg_color="black",
                                            command=self.myprofile,text_color="white",cursor="hand2")
        ok_Button.place(x=400, y=100)
    
    def myprofile(self):

        self.frame12=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame12.place(x=300, y=0, width=1300, height=1080)

        mycourse_label = customtkinter.CTkLabel(self.frame12, text="MYPROFILE", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="#263238", fg_color="orange",width=419)
        mycourse_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame12,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame12.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=7)

        self.frame_profile = customtkinter.CTkFrame(self.frame12,fg_color="light blue")
        self.frame_profile.place(x=200,y=100,width=700,height=600)

        # self.profile_frame = customtkinter.CTkFrame(self.frame_profile,fg_color="white")
        # self.profile_frame.place(x=500,y=20,width=120,height=120)

        logout_button=customtkinter.CTkButton(self.frame_profile,text='Logout',text_font=("Times new roman", 15, "bold"),text_color='white',
                                              command=self.logout,bg_color="black", fg_color="black",width=5)
        logout_button.place(x=250,y=550)

        change_password_button=customtkinter.CTkButton(self.frame_profile,text='Change password',text_font=("Times new roman", 15, "bold"),
                                                       text_color='white',command=self.chan_password,bg_color="black", fg_color="black",width=5)
        change_password_button.place(x=50,y=550)
        
        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
        my_cursor = connection.cursor()
   

        my_cursor.execute("select * from user")
        data = my_cursor.fetchall()

        for x in data:
            if self.access.get() == x[2]:
                userdomain_label = Label(self.frame_profile, text="Domain: ",font=("Times new roman", 15, "bold"),background='light blue',fg="black").grid(row=0,column=1,padx=10,pady=20,sticky=W)
                userdomain_entry = Label(self.frame_profile,text=x[0],font=("Times new roman", 15),cursor='hand2',foreground='black',background='light blue').grid(row=0,column=2,padx=5,sticky=W)

                userid_label = Label(self.frame_profile, text="ID: ", font=("Times new roman", 15, "bold"),background='light blue',fg="black").grid(row=1,column=1,padx=10,pady=20,sticky=W)
                userid_entry = Label(self.frame_profile,text=x[1],font=("Times new roman", 15),cursor='hand2',background='light blue').grid(row=1,column=2,padx=5,sticky=W)

                username_label = Label(self.frame_profile, text="Name: ", font=("Times new roman", 15, "bold"),background='light blue',fg="black").grid(row=2,column=1,padx=10,pady=20,sticky=W)
                username_entry = Label(self.frame_profile,text=x[2],font=("Times new roman", 15),cursor='hand2',background='light blue').grid(row=2,column=2,padx=5,sticky=W)

                userpass_label = Label(self.frame_profile, text="Password: ", font=("Times new roman", 15, "bold"),background='light blue',fg="black").grid(row=3,column=1,padx=10,pady=20,sticky=W)
                userpass_entry = Label(self.frame_profile,text=x[3],font=("Times new roman", 15),cursor='hand2',background='light blue').grid(row=3,column=2,padx=5,sticky=W)

                useremail_label = Label(self.frame_profile, text="Email ID:", font=("Times new roman", 15, "bold"),background='light blue',fg="black").grid(row=4,column=1,padx=10,pady=20,sticky=W)
                useremail_entry = Label(self.frame_profile,text=x[4],font=("Times new roman", 15),cursor='hand2',background='light blue').grid(row=4,column=2,padx=5,sticky=W)

                userphone_label = Label(self.frame_profile, text="Phone: ", font=("Times new roman", 15, "bold"),background='light blue',fg="black").grid(row=5,column=1,padx=10,pady=20,sticky=W)
                userphone_entry = Label(self.frame_profile,text=x[5],font=("Times new roman", 15),cursor='hand2',background='light blue').grid(row=5,column=2,padx=5,sticky=W)
          
        connection.commit()
        connection.close()
        

    def chan_password(self):

        from change_user_pass import change_password
        change = change_password(self.root)

    def Mycourse(self):

        self.frame13=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame13.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame13, text="MYCOURSE", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame13,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame13.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        frame_python = customtkinter.CTkFrame(self.frame13,bg_color="#FFFFFF",fg_color="#FFFFFF")
        frame_python.place(x=100, y=100,width=260,height=260) 
        self.img1 = ImageTk.PhotoImage(PIL.Image.open("images\\python.png"))
        self.label1 = Label(frame_python, image = self.img1).place(x=0,y=0)
        python_button = customtkinter.CTkButton(frame_python,command=self.python_file_menu,text="PYTHON",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        python_button.place(x=60,y=220)

        frame_java = customtkinter.CTkFrame(self.frame13,bg_color="#FFFFFF",fg_color="#FFFFFF")
        frame_java.place(x=500, y=100,width=260,height=260)
        self.img2 = ImageTk.PhotoImage(PIL.Image.open("images\\java.png"))
        self.label2 = Label(frame_java, image = self.img2).place(x=0,y=-20) 
        java_button = customtkinter.CTkButton(frame_java,text="JAVA",command=self.java_file_menu,text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_c = customtkinter.CTkFrame(self.frame13,bg_color="#FFFFFF",fg_color="#FFFFFF")
        frame_c.place(x=900, y=100,width=260,height=260)
        self.img3 = ImageTk.PhotoImage(PIL.Image.open("images\\c.png"))
        self.label3 = Label(frame_c, image = self.img3).place(x=0,y=0) 
        c_button = customtkinter.CTkButton(frame_c,text="C",text_color="white",command=self.c_file_menu,fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_jenkins = customtkinter.CTkFrame(self.frame13,bg_color="#FFFFFF",fg_color="#FFFFFF")
        frame_jenkins.place(x=100, y=400,width=260,height=260)
        self.img4 = ImageTk.PhotoImage(PIL.Image.open("images\\jenkins.png"))
        self.label4 = Label(frame_jenkins, image = self.img4).place(x=0,y=0) 
        jenkins_button = customtkinter.CTkButton(frame_jenkins,text="JENKINS",command=self.jenkins_file_menu,text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_docker = customtkinter.CTkFrame(self.frame13,bg_color="#FFFFFF",fg_color="#FFFFFF")
        frame_docker.place(x=500, y=400,width=260,height=260)
        self.img5 = ImageTk.PhotoImage(PIL.Image.open("images\\docker.png"))
        self.label5 = Label(frame_docker, image = self.img5).place(x=0,y=0) 
        docker_button = customtkinter.CTkButton(frame_docker,text="DOCKER",command=self.docker_file_menu,text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_aws = customtkinter.CTkFrame(self.frame13,bg_color="#FFFFFF",fg_color="#FFFFFF")
        frame_aws.place(x=900, y=400,width=260,height=260)
        self.img6 = ImageTk.PhotoImage(PIL.Image.open("images\\aws.png"))
        self.label6 = Label(frame_aws, image = self.img6).place(x=0,y=0) 
        aws_button = customtkinter.CTkButton(frame_aws,text="AWS",text_color="white",command=self.aws_file_menu,fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

    def python_file_menu(self):
   
        self.frame6=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame6.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame6, text="PYTHON MENU", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame6,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame6.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        self.frame_py_VIDEOS = customtkinter.CTkFrame(self.frame6,bg_color="#FFFFFF",fg_color="light green")
        self.frame_py_VIDEOS.place(x=200, y=100,width=260,height=260) 
        VIDEOS_button = customtkinter.CTkButton(self.frame_py_VIDEOS,command=self.python_video,text="VIDEOS",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        VIDEOS_button.place(x=60,y=220)
        self.v1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\video.jpeg"))
        self.v1_label1 = Label(self.frame_py_VIDEOS, image = self.v1_img1).place(x=0,y=10)

        
        frame_NOTES = customtkinter.CTkFrame(self.frame6,bg_color="#FFFFFF",fg_color="light green")
        frame_NOTES.place(x=700, y=100,width=260,height=260)
        self.n1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\notes.jpeg"))
        self.n1_label1 = Label(frame_NOTES, image = self.n1_img1).place(x=15,y=10)
        NOTES_button = customtkinter.CTkButton(frame_NOTES,text="NOTES",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        frame_ASSIGNMENT = customtkinter.CTkFrame(self.frame6,bg_color="#FFFFFF",fg_color="light green")
        frame_ASSIGNMENT.place(x=200, y=400,width=260,height=260)
        self.a1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\assignment.jpeg"))
        self.a1_label1 = Label(frame_ASSIGNMENT, image = self.a1_img1).place(x=0,y=20) 
        ASSIGNMENT_button = customtkinter.CTkButton(frame_ASSIGNMENT,command=self.python_assignment,text="ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        frame_SAMPLE = customtkinter.CTkFrame(self.frame6,bg_color="#FFFFFF",fg_color="light green")
        frame_SAMPLE.place(x=700, y=400,width=260,height=260)
        self.s1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\quiz.jpeg"))
        self.s1_label1 = Label(frame_SAMPLE, image = self.s1_img1).place(x=15,y=10) 
        SAMPLE_button = customtkinter.CTkButton(frame_SAMPLE,command=self.python_quiz,text="QUIZ",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)

        
    def python_video(self):
        
        s3 = boto3.resource('s3', region_name='us-east-2')
        bucket = s3.Bucket('files-apps')   
        object = bucket.Object('py_video.mp4') 
        object.download_file('video\\video2.mp4')

        self.frame_video=Frame(self.root,relief=GROOVE,bg="black")
        self.frame_video.place(x=0, y=0, width=1920, height=800)

        x_button=customtkinter.CTkButton(self.frame_video,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.delete_py,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=5)

        self.videoplayer = TkinterVideo(self.frame_video, scaled=True)
        self.videoplayer.load(r"video\\video2.mp4")
        self.videoplayer.place(x=50,y=50,width=1400,height=650)
        self.videoplayer.play()
        self.videoplayer.current_duration()

        play_button=customtkinter.CTkButton(self.frame_video,text='play',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.play_py,
                                         bg_color="#263238", fg_color="#263238",width=5)
        play_button.place(x=600,y=700)
        stop_button=customtkinter.CTkButton(self.frame_video,text='pause',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.pause_py,
                                         bg_color="#263238", fg_color="#263238",width=5)
        stop_button.place(x=700,y=700)

    def play_py(self):
        self.videoplayer.play()

    def pause_py(self):
        self.videoplayer.pause()

    def delete_py(self):
        self.frame_video.destroy
        home.remove(self)

    def remove(Self):
        os.remove("video\\video2.mp4")
        
    def python_file(self):

        self.frame7=Frame(self.root,relief=GROOVE,bg="#A8B9BF")
        self.frame7.place(x=300, y=0, width=1220, height=900)

        x_button=customtkinter.CTkButton(self.frame7,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame7.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=1170,y=6)

        text_box = Text(self.frame7,height=140,width=100,font=('times new roman',15) )
        text_box.pack(side=LEFT,expand=True,padx=80,pady=100)
        text_box.config(bg='#D9D8D7')

        reader = PdfReader("Files\python_course.pdf")
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            str(i+1)
            text = page.extract_text()
            text_box.insert(END,text)

        sb_ver = Scrollbar(self.frame7,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)

        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def python_assignment(self):
          
        self.frame_ass=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame_ass.place(x=300, y=0, width=1300, height=1080)
         
        assignment_label = customtkinter.CTkLabel(self.frame_ass, text="Weekly Assignment", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        assignment_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame_ass,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_ass.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        week1 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week1.place(x=200, y=100,width=260,height=260) 
        self.as1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week1.png"))
        self.v1_label1 = Label(week1, image = self.as1_img1).place(x=15,y=10)
        week1_button = customtkinter.CTkButton(week1,command=self.python_video,text="Week 1",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        week1_button.place(x=60,y=220)
        
        
        week2 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week2.place(x=700, y=100,width=260,height=260)
        self.as2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week2.jpeg"))
        self.n1_label1 = Label(week2, image = self.as2_img1).place(x=10,y=10)
        week2_button = customtkinter.CTkButton(week2,text="Week 2",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        week3 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week3.place(x=200, y=400,width=260,height=260)
        self.as3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week3.png"))
        self.a1_label1 = Label(week3, image = self.as3_img1).place(x=15,y=20) 
        week3_button = customtkinter.CTkButton(week3,text="Week 3",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        week4 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week4.place(x=700, y=400,width=260,height=260)
        self.as4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week4.png"))
        self.s1_label1 = Label(week4, image = self.as4_img1).place(x=15,y=10) 
        week4_button = customtkinter.CTkButton(week4,command=self.python_quiz,text="Week 4",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)
    
    def python_quiz(self):
        from python_quiz import PYTHON_Quiz
        q = PYTHON_Quiz(root)

    def java_file_menu(self):

        self.frame7=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame7.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame7, text="JAVA MENU", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=550, y=10)

        x_button=customtkinter.CTkButton(self.frame7,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame7.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=8)

        frame_VIDEOS = customtkinter.CTkFrame(self.frame7,bg_color="#FFFFFF",fg_color="light green")
        frame_VIDEOS.place(x=200, y=100,width=260,height=260) 
        self.v2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\video.jpeg"))
        self.v2_label1 = Label(frame_VIDEOS, image = self.v2_img1).place(x=0,y=10)
        VIDEOS_button = customtkinter.CTkButton(frame_VIDEOS,command=self.java_video,text="VIDEOS",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        VIDEOS_button.place(x=60,y=220)

        frame_NOTES = customtkinter.CTkFrame(self.frame7,bg_color="#FFFFFF",fg_color="light green")
        frame_NOTES.place(x=700, y=100,width=260,height=260)
        self.n2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\notes.jpeg"))
        self.n2_label1 = Label(frame_NOTES, image = self.n2_img1).place(x=15,y=10)
        NOTES_button = customtkinter.CTkButton(frame_NOTES,text="NOTES",text_color="white",command=self.java_file,fg_color="orange",
                                               bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_ASSIGNMENT = customtkinter.CTkFrame(self.frame7,bg_color="#FFFFFF",fg_color="light green")
        frame_ASSIGNMENT.place(x=200, y=400,width=260,height=260)
        self.a2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\assignment.jpeg"))
        self.a2_label1 = Label(frame_ASSIGNMENT, image = self.a2_img1).place(x=0,y=20) 
        ASSIGNMENT_button = customtkinter.CTkButton(frame_ASSIGNMENT,command=self.java_assignment,text="ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_SAMPLE = customtkinter.CTkFrame(self.frame7,bg_color="#FFFFFF",fg_color="light green")
        frame_SAMPLE.place(x=700, y=400,width=260,height=260)
        self.s2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\quiz.jpeg"))
        self.s2_label1 = Label(frame_SAMPLE, image = self.s2_img1).place(x=15,y=10)
        SAMPLE_button = customtkinter.CTkButton(frame_SAMPLE,command=self.java_quiz,text="QUIZ",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

    def java_video(self):
        
        self.frame_video1=Frame(self.root,relief=GROOVE,bg="black")
        self.frame_video1.place(x=0, y=0, width=1920, height=800)

        x_button=customtkinter.CTkButton(self.frame_video1,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_video1.destroy,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=5)

        videoplayer = TkinterVideo(self.frame_video1, scaled=True)
        videoplayer.load(r"video.mp4")
        videoplayer.pack(expand=True, fill="both",pady=50)
        videoplayer.play()

    def java_file(self):

        self.frame8=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame8.place(x=300, y=0, width=1300, height=1080)

        x_button=customtkinter.CTkButton(self.frame8,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame8.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=850,y=7)
        
        text_box = Text(self.frame8,height=140,width=100,font=('times new roman',15) )
        text_box.pack(side=LEFT,expand=True,padx=80,pady=100)
        text_box.config(bg='#D9D8D7')

        reader = PdfReader("Files\java.pdf")
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            str(i+1)
            text = page.extract_text()
            text_box.insert(END,text)

        sb_ver = Scrollbar(self.frame8,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)


        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def java_assignment(self):
          
        self.frame_ass=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame_ass.place(x=300, y=0, width=1300, height=1080)
         
        assignment_label = customtkinter.CTkLabel(self.frame_ass, text="Weekly Assignment", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        assignment_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame_ass,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_ass.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        week1 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week1.place(x=200, y=100,width=260,height=260) 
        self.as1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week1.png"))
        self.v1_label1 = Label(week1, image = self.as1_img1).place(x=15,y=10)
        week1_button = customtkinter.CTkButton(week1,command=self.python_video,text="Week 1",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        week1_button.place(x=60,y=220)
        
        
        week2 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week2.place(x=700, y=100,width=260,height=260)
        self.as2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week2.jpeg"))
        self.n1_label1 = Label(week2, image = self.as2_img1).place(x=10,y=10)
        week2_button = customtkinter.CTkButton(week2,text="Week 2",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        week3 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week3.place(x=200, y=400,width=260,height=260)
        self.as3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week3.png"))
        self.a1_label1 = Label(week3, image = self.as3_img1).place(x=15,y=20) 
        week3_button = customtkinter.CTkButton(week3,text="Week 3",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        week4 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week4.place(x=700, y=400,width=260,height=260)
        self.as4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week4.png"))
        self.s1_label1 = Label(week4, image = self.as4_img1).place(x=15,y=10) 
        week4_button = customtkinter.CTkButton(week4,command=self.python_quiz,text="Week 4",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)

    def java_quiz(self):
        from java_quiz import JAVA_QUIZ 
        q = JAVA_QUIZ()

    def c_file_menu(self):

        self.frame8=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame8.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame8, text="C MENU", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=550, y=10)

        x_button=customtkinter.CTkButton(self.frame8,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame8.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=8)

        frame_VIDEOS = customtkinter.CTkFrame(self.frame8,bg_color="#FFFFFF",fg_color="light green")
        frame_VIDEOS.place(x=200, y=100,width=260,height=260) 
        self.v3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\video.jpeg"))
        self.v3_label1 = Label(frame_VIDEOS, image = self.v3_img1).place(x=0,y=10)
        VIDEOS_button = customtkinter.CTkButton(frame_VIDEOS,command=self.c_video,text="VIDEOS",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        VIDEOS_button.place(x=60,y=220)

        frame_NOTES = customtkinter.CTkFrame(self.frame8,bg_color="#FFFFFF",fg_color="light green")
        frame_NOTES.place(x=700, y=100,width=260,height=260)
        self.n3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\notes.jpeg"))
        self.n3_label1 = Label(frame_NOTES, image = self.n3_img1).place(x=15,y=10)
        NOTES_button = customtkinter.CTkButton(frame_NOTES,text="NOTES",text_color="white",command=self.c_file,fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_ASSIGNMENT = customtkinter.CTkFrame(self.frame8,bg_color="#FFFFFF",fg_color="light green")
        frame_ASSIGNMENT.place(x=200, y=400,width=260,height=260)
        self.a3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\assignment.jpeg"))
        self.a3_label1 = Label(frame_ASSIGNMENT, image = self.a3_img1).place(x=0,y=20) 
        ASSIGNMENT_button = customtkinter.CTkButton(frame_ASSIGNMENT,command=self.c_assignment,text="ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_SAMPLE = customtkinter.CTkFrame(self.frame8,bg_color="#FFFFFF",fg_color="light green")
        frame_SAMPLE.place(x=700, y=400,width=260,height=260)
        self.s3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\quiz.jpeg"))
        self.s3_label1 = Label(frame_SAMPLE, image = self.s3_img1).place(x=15,y=10) 
        SAMPLE_button = customtkinter.CTkButton(frame_SAMPLE,command=self.c_quiz,text="QUIZ",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

    def c_video(self):
        
        self.frame_video2=Frame(self.root,relief=GROOVE,bg="black")
        self.frame_video2.place(x=0, y=0, width=1920, height=800)

        x_button=customtkinter.CTkButton(self.frame_video2,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_video2.destroy,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=5)

        videoplayer = TkinterVideo(self.frame_video2, scaled=True)
        videoplayer.load(r"video.mp4")
        videoplayer.pack(expand=True, fill="both",pady=50)
        videoplayer.play()
    
    def c_file(self):

        self.frame9=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame9.place(x=300, y=0, width=1300, height=1080)

        x_button=customtkinter.CTkButton(self.frame9,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame9.destroy,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=850,y=7)
        
        text_box = Text(self.frame9,height=140,width=100,font=('times new roman',15) )
        text_box.pack(side=LEFT,expand=True,padx=80,pady=100)
        text_box.config(bg='#D9D8D7')

        reader = PdfReader("Files\c.pdf")
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            str(i+1)
            text = page.extract_text()
            text_box.insert(END,text)

        sb_ver = Scrollbar(self.frame9,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)

        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def c_assignment(self):
          
        self.frame_ass=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame_ass.place(x=300, y=0, width=1300, height=1080)
         
        assignment_label = customtkinter.CTkLabel(self.frame_ass, text="Weekly Assignment", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        assignment_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame_ass,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_ass.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        week1 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week1.place(x=200, y=100,width=260,height=260) 
        self.as1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week1.png"))
        self.v1_label1 = Label(week1, image = self.as1_img1).place(x=15,y=10)
        week1_button = customtkinter.CTkButton(week1,command=self.python_video,text="Week 1",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        week1_button.place(x=60,y=220)
        
        
        week2 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week2.place(x=700, y=100,width=260,height=260)
        self.as2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week2.jpeg"))
        self.n1_label1 = Label(week2, image = self.as2_img1).place(x=10,y=10)
        week2_button = customtkinter.CTkButton(week2,text="Week 2",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        week3 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week3.place(x=200, y=400,width=260,height=260)
        self.as3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week3.png"))
        self.a1_label1 = Label(week3, image = self.as3_img1).place(x=15,y=20) 
        week3_button = customtkinter.CTkButton(week3,text="Week 3",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        week4 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week4.place(x=700, y=400,width=260,height=260)
        self.as4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week4.png"))
        self.s1_label1 = Label(week4, image = self.as4_img1).place(x=15,y=10) 
        week4_button = customtkinter.CTkButton(week4,command=self.python_quiz,text="Week 4",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)
        
    def c_quiz(self):
        from c_quiz import C_Quiz 
        q = C_Quiz()

    def aws_file_menu(self):

        self.frame16=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame16.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame16, text="AWS MENU", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=550, y=10)

        x_button=customtkinter.CTkButton(self.frame16,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame16.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=8)

        frame_VIDEOS = customtkinter.CTkFrame(self.frame16,bg_color="#FFFFFF",fg_color="light green")
        frame_VIDEOS.place(x=200, y=100,width=260,height=260) 
        self.v4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\video.jpeg"))
        self.v4_label1 = Label(frame_VIDEOS, image = self.v4_img1).place(x=0,y=10)
        VIDEOS_button = customtkinter.CTkButton(frame_VIDEOS,command=self.aws_video,text="VIDEOS",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        VIDEOS_button.place(x=60,y=220)

        frame_NOTES = customtkinter.CTkFrame(self.frame16,bg_color="#FFFFFF",fg_color="light green")
        frame_NOTES.place(x=700, y=100,width=260,height=260)
        self.n4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\notes.jpeg"))
        self.n4_label1 = Label(frame_NOTES, image = self.n4_img1).place(x=15,y=10)
        NOTES_button = customtkinter.CTkButton(frame_NOTES,text="NOTES",text_color="white",command=self.aws_file,fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_ASSIGNMENT = customtkinter.CTkFrame(self.frame16,bg_color="#FFFFFF",fg_color="light green")
        frame_ASSIGNMENT.place(x=200, y=400,width=260,height=260)
        self.a4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\assignment.jpeg"))
        self.a4_label1 = Label(frame_ASSIGNMENT, image = self.a4_img1).place(x=0,y=20) 
        ASSIGNMENT_button = customtkinter.CTkButton(frame_ASSIGNMENT,command=self.aws_assignment,text="ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_SAMPLE = customtkinter.CTkFrame(self.frame16,bg_color="#FFFFFF",fg_color="light green")
        frame_SAMPLE.place(x=700, y=400,width=260,height=260)
        self.s4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\quiz.jpeg"))
        self.s4_label1 = Label(frame_SAMPLE, image = self.s4_img1).place(x=15,y=10)
        SAMPLE_button = customtkinter.CTkButton(frame_SAMPLE,command=self.aws_quiz,text="QUIZ",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

    def aws_video(self):

        
        self.frame_video3=Frame(self.root,relief=GROOVE,bg="black")
        self.frame_video3.place(x=0, y=0, width=1920, height=800)

        x_button=customtkinter.CTkButton(self.frame_video3,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_video3.destroy,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=5)

        videoplayer = TkinterVideo(self.frame_video3, scaled=True)
        videoplayer.load(r"video.mp4")
        videoplayer.pack(expand=True, fill="both",pady=50)
        videoplayer.play()

    def aws_file(self):

        self.frame5=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame5.place(x=300, y=0, width=1300, height=1080)

        x_button=customtkinter.CTkButton(self.frame5,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame5.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=850,y=7)
        
        text_box = Text(self.frame5,height=140,width=100,font=('times new roman',15) )
        text_box.pack(side=LEFT,expand=True,padx=80,pady=100)
        text_box.config(bg='#D9D8D7')

        reader = PdfReader("Files\Aws_course.pdf")
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            str(i+1)
            text = page.extract_text()
            text_box.insert(END,text)

        sb_ver = Scrollbar(self.frame5,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)

        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def aws_assignment(self):
          
        self.frame_ass=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame_ass.place(x=300, y=0, width=1300, height=1080)
         
        assignment_label = customtkinter.CTkLabel(self.frame_ass, text="Weekly Assignment", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        assignment_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame_ass,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_ass.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        week1 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week1.place(x=200, y=100,width=260,height=260) 
        self.as1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week1.png"))
        self.v1_label1 = Label(week1, image = self.as1_img1).place(x=15,y=10)
        week1_button = customtkinter.CTkButton(week1,command=self.python_video,text="Week 1",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        week1_button.place(x=60,y=220)
        
        
        week2 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week2.place(x=700, y=100,width=260,height=260)
        self.as2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week2.jpeg"))
        self.n1_label1 = Label(week2, image = self.as2_img1).place(x=10,y=10)
        week2_button = customtkinter.CTkButton(week2,text="Week 2",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        week3 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week3.place(x=200, y=400,width=260,height=260)
        self.as3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week3.png"))
        self.a1_label1 = Label(week3, image = self.as3_img1).place(x=15,y=20) 
        week3_button = customtkinter.CTkButton(week3,text="Week 3",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        week4 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week4.place(x=700, y=400,width=260,height=260)
        self.as4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week4.png"))
        self.s1_label1 = Label(week4, image = self.as4_img1).place(x=15,y=10) 
        week4_button = customtkinter.CTkButton(week4,command=self.python_quiz,text="Week 4",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)
        
    def aws_quiz(self):
        from aws_quiz import AWS_Quiz 
        q = AWS_Quiz()

    def docker_file_menu(self):

        self.frame17=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame17.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame17, text="DOCKER MENU", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=550, y=10)

        x_button=customtkinter.CTkButton(self.frame17,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame17.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=8)

        frame_VIDEOS = customtkinter.CTkFrame(self.frame17,bg_color="#FFFFFF",fg_color="light green")
        frame_VIDEOS.place(x=200, y=100,width=260,height=260) 
        self.v5_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\video.jpeg"))
        self.v5_label1 = Label(frame_VIDEOS, image = self.v5_img1).place(x=0,y=10)
        VIDEOS_button = customtkinter.CTkButton(frame_VIDEOS,command=self.docker_video,text="VIDEOS",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        VIDEOS_button.place(x=60,y=220)

        frame_NOTES = customtkinter.CTkFrame(self.frame17,bg_color="#FFFFFF",fg_color="light green")
        frame_NOTES.place(x=700, y=100,width=260,height=260)
        self.n5_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\notes.jpeg"))
        self.n5_label1 = Label(frame_NOTES, image = self.n5_img1).place(x=15,y=10)
        NOTES_button = customtkinter.CTkButton(frame_NOTES,text="NOTES",text_color="white",command=self.docker_file,fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_ASSIGNMENT = customtkinter.CTkFrame(self.frame17,bg_color="#FFFFFF",fg_color="light green")
        frame_ASSIGNMENT.place(x=200, y=400,width=260,height=260)
        self.a5_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\assignment.jpeg"))
        self.a5_label1 = Label(frame_ASSIGNMENT, image = self.a5_img1).place(x=0,y=20) 
        ASSIGNMENT_button = customtkinter.CTkButton(frame_ASSIGNMENT,command=self.docker_assignment,text="ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_SAMPLE = customtkinter.CTkFrame(self.frame17,bg_color="#FFFFFF",fg_color="light green")
        frame_SAMPLE.place(x=700, y=400,width=260,height=260)
        self.s5_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\quiz.jpeg"))
        self.s5_label1 = Label(frame_SAMPLE, image = self.s5_img1).place(x=15,y=10)
        SAMPLE_button = customtkinter.CTkButton(frame_SAMPLE,command=self.docker_quiz,text="QUIZ",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

    def docker_video(self):
        
        self.frame_video4=Frame(self.root,relief=GROOVE,bg="black")
        self.frame_video4.place(x=0, y=0, width=1920, height=800)

        x_button=customtkinter.CTkButton(self.frame_video4,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_video4.destroy,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=5)

        videoplayer = TkinterVideo(self.frame_video4, scaled=True)
        videoplayer.load(r"video.mp4")
        videoplayer.pack(expand=True, fill="both",pady=50)
        videoplayer.play()
    
    def docker_file(self):

        self.frame10=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame10.place(x=300, y=0, width=1300, height=1080)

        x_button=customtkinter.CTkButton(self.frame10,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame10.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=850,y=7)
        
        text_box = Text(self.frame10,height=140,width=100,font=('times new roman',15) )
        text_box.pack(side=LEFT,expand=True,padx=80,pady=100)
        text_box.config(bg='#D9D8D7')

        reader = PdfReader("Files\docker.pdf")
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            str(i+1)
            text = page.extract_text()
            text_box.insert(END,text)

        sb_ver = Scrollbar(self.frame10,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)

        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def docker_assignment(self):
          
        self.frame_ass=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame_ass.place(x=300, y=0, width=1300, height=1080)
         
        assignment_label = customtkinter.CTkLabel(self.frame_ass, text="Weekly Assignment", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        assignment_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame_ass,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_ass.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        week1 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week1.place(x=200, y=100,width=260,height=260) 
        self.as1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week1.png"))
        self.v1_label1 = Label(week1, image = self.as1_img1).place(x=15,y=10)
        week1_button = customtkinter.CTkButton(week1,command=self.python_video,text="Week 1",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        week1_button.place(x=60,y=220)
        
        
        week2 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week2.place(x=700, y=100,width=260,height=260)
        self.as2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week2.jpeg"))
        self.n1_label1 = Label(week2, image = self.as2_img1).place(x=10,y=10)
        week2_button = customtkinter.CTkButton(week2,text="Week 2",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        week3 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week3.place(x=200, y=400,width=260,height=260)
        self.as3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week3.png"))
        self.a1_label1 = Label(week3, image = self.as3_img1).place(x=15,y=20) 
        week3_button = customtkinter.CTkButton(week3,text="Week 3",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        week4 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week4.place(x=700, y=400,width=260,height=260)
        self.as4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week4.png"))
        self.s1_label1 = Label(week4, image = self.as4_img1).place(x=15,y=10) 
        week4_button = customtkinter.CTkButton(week4,command=self.python_quiz,text="Week 4",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)
        
    def docker_quiz(self):
        from docker_quiz import DOCKER_Quiz 
        q = DOCKER_Quiz()

    def jenkins_file_menu(self):

        self.frame18=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame18.place(x=300, y=0, width=1300, height=1080)
         
        mycourse_label = customtkinter.CTkLabel(self.frame18, text="JENINS MENU", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=550, y=10)

        x_button=customtkinter.CTkButton(self.frame18,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame18.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=8)

        frame_VIDEOS = customtkinter.CTkFrame(self.frame18,bg_color="#FFFFFF",fg_color="light green")
        frame_VIDEOS.place(x=200, y=100,width=260,height=260) 
        self.v6_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\video.jpeg"))
        self.v6_label1 = Label(frame_VIDEOS, image = self.v6_img1).place(x=0,y=10)
        VIDEOS_button = customtkinter.CTkButton(frame_VIDEOS,command=self.jenkins_video,text="VIDEOS",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        VIDEOS_button.place(x=60,y=220)

        frame_NOTES = customtkinter.CTkFrame(self.frame18,bg_color="#FFFFFF",fg_color="light green")
        frame_NOTES.place(x=700, y=100,width=260,height=260)
        self.n6_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\notes.jpeg"))
        self.n6_label1 = Label(frame_NOTES, image = self.n6_img1).place(x=15,y=10)
        NOTES_button = customtkinter.CTkButton(frame_NOTES,text="NOTES",text_color="white",command=self.jenkins_file,fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_ASSIGNMENT = customtkinter.CTkFrame(self.frame18,bg_color="#FFFFFF",fg_color="light green")
        frame_ASSIGNMENT.place(x=200, y=400,width=260,height=260)
        self.a6_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\assignment.jpeg"))
        self.a6_label1 = Label(frame_ASSIGNMENT, image = self.a6_img1).place(x=0,y=20)  
        ASSIGNMENT_button = customtkinter.CTkButton(frame_ASSIGNMENT,command=self.jenkins_assignment,text="ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

        frame_SAMPLE = customtkinter.CTkFrame(self.frame18,bg_color="#FFFFFF",fg_color="light green")
        frame_SAMPLE.place(x=700, y=400,width=260,height=260)
        self.s6_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\quiz.jpeg"))
        self.s6_label1 = Label(frame_SAMPLE, image = self.s6_img1).place(x=15,y=10)
        SAMPLE_button = customtkinter.CTkButton(frame_SAMPLE,command=self.jenkins_quiz,text="SAMPLE ASSIGNMENT",text_color="white",fg_color="orange",bg_color="black",cursor="hand2").place(x=60,y=220)

    def jenkins_video(self):
        
        self.frame_video5=Frame(self.root,relief=GROOVE,bg="black")
        self.frame_video5.place(x=0, y=0, width=1920, height=800)

        x_button=customtkinter.CTkButton(self.frame_video5,text='Exit',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_video5.destroy,
                                         bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=5)

        videoplayer = TkinterVideo(self.frame_video5, scaled=True)
        videoplayer.load(r"video.mp4")
        videoplayer.pack(expand=True, fill="both",pady=50)
        videoplayer.play()
    
    def jenkins_file(self):

        self.frame11=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame11.place(x=300, y=0, width=1300, height=1080)

        x_button=customtkinter.CTkButton(self.frame11,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame11.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=850,y=7)
        
        text_box = Text(self.frame11,height=140,width=100,font=('times new roman',15) )
        text_box.pack(side=LEFT,expand=True,padx=80,pady=100)
        text_box.config(bg='#D9D8D7')

        reader = PdfReader("Files\jenkins.pdf")
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            str(i+1)
            text = page.extract_text()
            text_box.insert(END,text)

        sb_ver = Scrollbar(self.frame11,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)

        text_box.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=text_box.yview)

    def jenkins_assignment(self):
          
        self.frame_ass=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame_ass.place(x=300, y=0, width=1300, height=1080)
         
        assignment_label = customtkinter.CTkLabel(self.frame_ass, text="Weekly Assignment", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        assignment_label.place(x=350, y=10)

        x_button=customtkinter.CTkButton(self.frame_ass,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame_ass.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=770,y=8)

        week1 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week1.place(x=200, y=100,width=260,height=260) 
        self.as1_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week1.png"))
        self.v1_label1 = Label(week1, image = self.as1_img1).place(x=15,y=10)
        week1_button = customtkinter.CTkButton(week1,command=self.python_video,text="Week 1",text_color="white",fg_color="orange",bg_color="black",cursor="hand2")
        week1_button.place(x=60,y=220)
        
        
        week2 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week2.place(x=700, y=100,width=260,height=260)
        self.as2_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week2.jpeg"))
        self.n1_label1 = Label(week2, image = self.as2_img1).place(x=10,y=10)
        week2_button = customtkinter.CTkButton(week2,text="Week 2",text_color="white",command=self.python_file,fg_color="orange",bg_color="black",
                                               cursor="hand2").place(x=60,y=220)

        week3 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week3.place(x=200, y=400,width=260,height=260)
        self.as3_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week3.png"))
        self.a1_label1 = Label(week3, image = self.as3_img1).place(x=15,y=20) 
        week3_button = customtkinter.CTkButton(week3,text="Week 3",text_color="white",fg_color="orange",bg_color="black",
                                                    cursor="hand2").place(x=60,y=220)

        week4 = customtkinter.CTkFrame(self.frame_ass,bg_color="#FFFFFF",fg_color="light green")
        week4.place(x=700, y=400,width=260,height=260)
        self.as4_img1 = ImageTk.PhotoImage(PIL.Image.open("images\\week4.png"))
        self.s1_label1 = Label(week4, image = self.as4_img1).place(x=15,y=10) 
        week4_button = customtkinter.CTkButton(week4,command=self.python_quiz,text="Week 4",text_color="white",fg_color="orange",
                                                bg_color="black",cursor="hand2").place(x=60,y=220)
        
    def jenkins_quiz(self):
        from jenkins_quiz import JENKINS_Quiz 
        q = JENKINS_Quiz()

    def Feedback(self):

        self.frame14=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame14.place(x=300, y=0, width=1300, height=1080)

        self.img7 = ImageTk.PhotoImage(PIL.Image.open("images\\feedback_back.jpg"))
        self.label2 = Label(self.frame14, image = self.img7).place(x=-100,y=-100,width=1920,height=1080)
        mycourse_label = customtkinter.CTkLabel(self.frame14, text="FEEDBACK", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="#263238", fg_color="orange",width=419)
        mycourse_label.place(x=450, y=10)

        x_button=customtkinter.CTkButton(self.frame14,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame14.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=850,y=7)

        frame_feedback = customtkinter.CTkFrame(self.frame14,fg_color="green")
        frame_feedback.place(x=300,y=200,width=700,height=300)
         
        self.user_id_label = customtkinter.CTkLabel(self.frame14, text="USER ID:", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="#263238", fg_color="orange",width=419)
        self.user_id_label.place(x=300, y=150,width=150)
        self.user_id_Entry = customtkinter.CTkEntry(self.frame14, text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="black", fg_color="white",width=419)
        self.user_id_Entry.place(x=500, y=150)

        self.feedback_Entry = customtkinter.CTkEntry(frame_feedback,text_font=("Times new roman",15),bg_color="#263238",fg_color="#FFFFFF",text_color="black")
        self.feedback_Entry.place(x=80, y=40,width=550,height=200)
    
        ok_button = customtkinter.CTkButton(frame_feedback,text="OK",command=lambda: self.user_feedback(self.feedback_Entry.get(),self.user_id_Entry.get()),fg_color="orange",bg_color="black",text_color="white")
        ok_button.place(x=320,y=250)
        clear_button = customtkinter.CTkButton(frame_feedback,text="CLEAR",command=self.clear_text,fg_color="orange",bg_color="black",text_color="white")
        clear_button.place(x=480,y=250)

    def clear_text(self):
        self.feedback_Entry.delete(0, END)

    def user_feedback(self,feedback,user_id):
    
        connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='kbportal', port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("update feedback set f_feedback=%s where u_id=%s", (feedback,user_id))
        connection.commit()
        connection.close()
        #messagebox.showinfo("SUCCESS","Successfully updated")

    def user_privatefile_verify(self):

        self.frame5=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame5.place(x=300, y=0, width=1300, height=1080)

        self.frame6=customtkinter.CTkFrame(self.frame5,relief=GROOVE,fg_color="light blue",bg_color="light blue")
        self.frame6.place(x=0,y=0,width=1300,height=60)

        verify_label=customtkinter.CTkLabel(self.frame5,text="Verify",text_font=("Times new roman",15,"bold"),fg_color="light blue",
                                               text_color="black",bg_color="light blue")
        verify_label.place(x=400, y=10) 

        x_button=customtkinter.CTkButton(self.frame5,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame5.destroy,bg_color="#263238", fg_color="#263238",width=5)
        x_button.place(x=970,y=7)

        self.access1  = StringVar()
        userid_Label = customtkinter.CTkLabel(self.frame5,text="User ID:",text_font=("Times new roman",15),bg_color="#263238",fg_color="#263238",
                                                text_color="white").place(x=20, y=100)  
        userid_Entry = customtkinter.CTkEntry(self.frame5,text=self.access1,text_font=("Times new roman",15),bg_color="#263238",fg_color="white",
                                                text_color="black").place(x=180, y=100)

        ok_Button = customtkinter.CTkButton(self.frame5, text="Ok",text_font=("Times new roman",15),bg_color="black",fg_color="black",
                                            command=self.Privatefile,text_color="white",cursor="hand2")
        ok_Button.place(x=400, y=100)

    def Privatefile(self):

        self.frame15=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        self.frame15.place(x=300, y=0, width=1300, height=1080)
        
        mycourse_label = customtkinter.CTkLabel(self.frame15, text="PRIVATE FILE", text_font=("Times new roman", 15, "bold"),text_color='black',bg_color="orange", fg_color="orange",width=419)
        mycourse_label.place(x=450, y=10)

        x_button=customtkinter.CTkButton(self.frame15,text='x',text_font=("Times new roman", 15, "bold"),text_color='#FFFFFF',command=self.frame15.destroy,bg_color="black", fg_color="#263238",width=5)
        x_button.place(x=870,y=8)

        self.frame_upload = customtkinter.CTkFrame(self.frame15,fg_color="white")
        self.frame_upload.place(x=300,y=200,width=700,height=300)
    
        upload_button = customtkinter.CTkButton( self.frame_upload,command=lambda: self.upload_files(self.access1.get()),text="UPLOAD",fg_color="orange",bg_color="black",text_color="white")
        upload_button.place(x=150,y=250)

        download_button = customtkinter.CTkButton( self.frame_upload,command=lambda:self.download_files(self.access1.get()),text="DOWNLOAD",fg_color="orange",bg_color="black",text_color="white")
        download_button.place(x=320,y=250)

        delete_button = customtkinter.CTkButton( self.frame_upload,command=lambda: self.delete_file(self.access1.get()),text="DELETE",fg_color="orange",
                                                bg_color="black",text_color="white")
        delete_button.place(x=490,y=250)
        

    def upload_files(self,p_id):

        if p_id == '1':
            s3 = boto3.resource('s3') 
            bucket1 = s3.Bucket('user2--bucket')
            file = filedialog.askopenfilename(title='select file',filetypes=(("PDF File","*.PDF"),("All Files","*.*")))
            bucket1.upload_file(file,file)

            file_label1 = customtkinter.CTkLabel( self.frame_upload,text=file,fg_color="black",bg_color="black",text_color="white")
            file_label1.place(x=100,y=100)
        
            messagebox.showinfo("SUCCESS","Successfully Uploaded")

        elif p_id == '2':
            s3_1 = boto3.resource('s3') 
            bucket1 = s3_1.Bucket('user3--bucket')
            file = filedialog.askopenfilename(title='select file',filetypes=(("PDF File","*.PDF"),("All Files","*.*")))
            bucket1.upload_file(file,file)

            file_label1 = customtkinter.CTkLabel( self.frame_upload,text=file,fg_color="black",bg_color="black",text_color="white")
            file_label1.place(x=100,y=100)
        
            messagebox.showinfo("SUCCESS","Successfully Uploaded")

    def download_files(self,p_id):

        if p_id == '1':
            s3 = boto3.resource('s3') 
            bucket1 = s3.Bucket('user2--bucket')

            bucket1.download_file('C:/Users/DELL/Documents/col-project/Files/python_course.pdf', r'C:\Users\DELL\Downloads\python_course1.pdf')

            messagebox.showinfo("SUCCESS","Successfully Downloaded")
        elif p_id == '2':
            s3_1 = boto3.resource('s3') 
            bucket1 = s3_1.Bucket('user3--bucket')
            bucket1.download_file('C:/Users/DELL/Documents/col-project/Files/java.pdf', r'C:\Users\DELL\Downloads\java.pdf')

            messagebox.showinfo("SUCCESS","Successfully Downloaded")            

    def delete_file(self,p_id):
        if p_id == '1':
            s3 = boto3.resource('s3')
            s3.Object('user2--bucket', 'C:/Users/DELL/Documents/col-project/Files/python_course.pdf').delete()
            file_label1 = customtkinter.CTkLabel( self.frame_upload,text='',fg_color="white",bg_color="white",text_color="white")
            file_label1.place(x=100,y=100,width=1000)
            messagebox.showinfo("SUCCESS","Successfully deleted")

        elif p_id == '2':
            s3_1 = boto3.resource('s3')
            s3_1.Object('user2--bucket', 'C:/Users/DELL/Documents/col-project/Files/java_course.pdf').delete()
            file_label2 = customtkinter.CTkLabel( self.frame_upload,text='',fg_color="white",bg_color="white",text_color="white")
            file_label2.place(x=100,y=100,width=1000)
            messagebox.showinfo("SUCCESS","Successfully deleted")
            
if __name__ == '__main__':
    root=Tk()
    obj=home(root)
    root.mainloop()