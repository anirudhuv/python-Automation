import os,shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
app=ctk.CTk()
app.geometry("568x400")
l1=ctk.CTkLabel(app,text="File Organizer",font=('Aerial', 18 ))
l1.pack()
def select_folder():
   global pathv
   pathv= filedialog.askdirectory(title="Select a File")
   ctk.CTkLabel(app, text=pathv, font=('calibre',10, 'bold')).pack()
   print(pathv)
   
#file organizer

def file_organizer():
   audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv",".mpeg")
   video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")
   img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

   doc= ('.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv')
   
   Comp= (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip")
	

   def is_audio(file):
     return os.path.splitext(file)[1] in audio

   def is_video(file):
      return os.path.splitext(file)[1] in video

   def is_image(file):
      return os.path.splitext(file)[1] in img

   def is_doc(file):
      return os.path.splitext(file)[1] in doc
   def is_comp(file):
      return os.path.splitext(file)[1] in Comp

   os.chdir(pathv)
#creating folders
   def createfol(pathv,f):
      fldr_path=os.path.join(pathv,f)
      os.makedirs(fldr_path,exist_ok=True)
      return fldr_path

   def fld_m(pathv,fldr_name):
      fld_path=[]
      for f in fldr_name:
         cf=createfol(pathv,f)
         fld_path.append(cf)
      return fld_path

   fldr_name=['audio', 'video', 'image', 'doc','Comp']

   path_list=fld_m(pathv,fldr_name)
   print(path_list[1])    
    
#organinzing
   for  f in os.listdir():
      if is_audio(f):
         shutil.move(f,path_list[0])
      elif is_video(f):
         shutil.move(f,path_list[1])  
      elif is_image(f):
         shutil.move(f,path_list[2])
      elif is_doc(f):
         shutil.move(f,path_list[3])           
      elif is_comp(f):
         shutil.move(f,path_list[4])
   return
    
    
        
l2=ctk.CTkLabel(app, text="Click the Button to Select a File", font=('calibre',30, 'bold'))
l2.pack(padx=20)
button= ctk.CTkButton(app, text="Select", command= select_folder)
button.pack(ipadx=5, pady=15)
b2=ctk.CTkButton(app, text="Submit", command= file_organizer)
b2.pack()
app.mainloop()
