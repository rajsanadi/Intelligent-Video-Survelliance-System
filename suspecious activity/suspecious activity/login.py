import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="grey")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("login")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('2.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



def registration():
    from subprocess import call
    call(["python","register.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT id FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()
         id=list(result[0])
         print(str(id))
         with open(r"id.txt", 'w') as f:
                  id1=f.write(str(id[0]))
                  print(id1)
         # f1 = open("id.txt","w")
         # id1 = f1.read(result)
         
         #f1.close()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_Master.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


# bg1_icon=ImageTk.PhotoImage(file="b.jpg")

bg_icon=ImageTk.PhotoImage(file="L.jpg")
user_icon=ImageTk.PhotoImage(file="l1.png")
pass_icon=ImageTk.PhotoImage(file="p1.jpg")
        
# bg_lbl=tk.Label(root,image=bg_icon, width=600,height=550)
# bg_lbl.place(x=50,y=40)
        
title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="gray",fg="white")
title.place(x=640,y=150,width=250)
        
# Login_frame=tk.Frame(root,bg="#1874CD")
# Login_frame.place(x=500,y=250)
        
# logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(root,text="Username",image=user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").place(x=550,y=250)
txtuser=tk.Entry(root,bd=5,textvariable=username,font=("",15))
txtuser.place(x=750,y=250)
        
lblpass=tk.Label(root,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").place(x=550,y=350)
txtpass=tk.Entry(root,bd=5,textvariable=password,show="*",font=("",15))
txtpass.place(x=750,y=350)
        
btn_log=tk.Button(root,text="Login",command=login,width=14,font=("Times new roman", 14, "bold"),bg="gray",fg="white")
btn_log.place(x=780,y=430)
btn_reg=tk.Button(root,text="Create Account",command=registration,width=14,font=("Times new roman", 14, "bold"),bg="red",fg="white")
btn_reg.place(x=580,y=430)
        
        
       
        # Login Function       




    
def window():
  root.destroy()
  
  







root.mainloop()