# from tkinter import *
# from PyPDF2 import PdfReader

# ws = Tk()
# ws.title('Pythonrootdes')
# ws.geometry('400x300')
# ws.config(bg='#5F734C')

# frame = Frame(
#     ws,
#     bg='#A8B9BF'
#     )

# text_box = Text(ws,height=13,width=32,font=(12)  )
# text_box.pack(side=LEFT,expand=True)
# text_box.config(bg='#D9D8D7')

# reader = PdfReader("Files\python_course.pdf")
# number_of_pages = len(reader.pages)
# # page = reader.pages[1]
# for i in range(number_of_pages):
#     page = reader.pages[i]
#     str(i+1)
#     text = page.extract_text()
#     # print(text)
#     text_box.insert(END,text)

# sb_ver = Scrollbar( ws,orient=VERTICAL)

# sb_ver.pack(side=RIGHT, fill=Y)

# text_box.config(yscrollcommand=sb_ver.set)
# sb_ver.config(command=text_box.yview)


# ws.mainloop()


import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"video.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()