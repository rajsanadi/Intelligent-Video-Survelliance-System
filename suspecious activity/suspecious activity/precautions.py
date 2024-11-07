import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("SUSPICIOUS ACTIVITY DETECTION SYSTEM")

#####For background Image
#loading the images
img=ImageTk.PhotoImage(Image.open("s2.jpg"))

img2=ImageTk.PhotoImage(Image.open("s3.jpg"))

img3=ImageTk.PhotoImage(Image.open("s4.jpg"))

image2 =Image.open('s2.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=100, y=200)


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x=1


# function to change to next image
def move():
    global x
    if x == 4:
            x = 1
    if x == 1:
        logo_label.config(image=img)
    elif x == 2:
        logo_label.config(image=img2)
    elif x == 3:
        logo_label.config(image=img3)
    x = x+1
    root.after(2000, move)
  
# calling the function
move()

# calling the function
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="light blue")
canvas.pack()
canvas.place(x=0, y=0)
text_var="INTELLIGENT VIDEO SURVEILLANCE SYSTEM"
text=canvas.create_text(0,-2000,text=text_var,font=('ittalian',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 50
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling


#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)



frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=300, height=600, bd=5, font=('times', 14, ' bold '),bg="grey")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=120)




def update_label1(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=600)
    
    image2 =Image.open('p2.jpg')
    image2 =image2.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=200, y=200)
    
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def update_cal(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=350, y=400)
    
    
    
###########################################################################



        
        
        
               
               
               



def Fighting():
    
    label=tk.Label(root,text='''Suspicious human activities like fighting, shooting,
                   fire have got serious security concern in public places because 
                   of a steep surge in these types of cases all around. CCTV cameras 
                   are generally installed at public places like malls, railway stations; 
                   but evidences suggest that only availability of these cameras are not 
                   very effective unless the video feeds are constantly monitored. 
                   Therefore, we intend to build an automated and intelligent video 
                   surveillance system to detect the suspicious human activities, 
                   followed by an alert generation.
''',width=80,bg="white",fg="black",height=30)
    label.place(x=500,y=200)
    
    
        
def Accident():

    label=tk.Label(root,text='''Traveling is one of the basic needs of every 
                   person who lives in cities or villages. 
                   There are several ways to travel from one place to 
                   another by air, water, rail, and road in various types 
                   of vehicle, e.g., cars, motorbikes, buses, and trucks.
                   Roads are the foremost source of linking between cities 
                   and villages.

''',width=80,bg="white",fg="black",height=30)
    label.place(x=500,y=200)
    
def Robbery():

    label=tk.Label(root,text='''A major purpose of video surveillance
                   is the detection of unusual situations such as traffic 
                   accidents, robberies, or illicit activity.
                   The proposed system is concerned with the
                   development of a surveillance video framework 
                   in the residential area to detect any type of 
                   suspicious robbery activity.
''',width=80,bg="white",fg="black",height=30)
    label.place(x=500,y=200)
    
def Theft():

    label=tk.Label(root,text='''Theft is a common criminal activity 
                   that is prevailing over the years and is increasing 
                   day by day. To tackle this problem, many surveillance 
                   systems have been introduced in the market. Some are 
                   simply based on video surveillance monitored by a human
                   while some are AI-based capable of detecting suspicious
                   activity and raising an alarm. 
''',width=80,bg="white",fg="black",height=30)
    label.place(x=500,y=200)
    
def Fraud():

    label=tk.Label(root,text='''Fraud detection is a process to 
                   identify deceptive activities within an organization.
                   It deals with discovering any illegitimate actions as
                   early as possible, thus enabling a swift response and
                   minimization of damage.It combines machine learning 
                   with statistical models to identify suspicious patterns,
                   guaranteeing compliance and minimizing damage from
                   potential fraudulent activity.
''',width=80,bg="white",fg="black",height=30)
    label.place(x=500,y=200)
    
def pre():
  
    from subprocess import call
    call(['python','GUI_Master.py'])

 #   label=tk.Label(root,text='''Blood Plates, Crohn's Disease--Swelling of the tissues
#''',width=100,bg="white",fg="black",height=30)
 #   label.place(x=500,y=200)
    
#def Wood_Sorel():

 #   label=tk.Label(root,text='''Liver and Digestive Disorders
#''',width=100,bg="white",fg="black",height=30)
 #   label.place(x=500,y=200)
    

#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text="Fighting", command= Fighting, width=20, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=10)

button2 = tk.Button(frame_alpr, text="Accident", command=Accident, width=20, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=90)

button3 = tk.Button(frame_alpr, text="Robbery", command=Robbery, width=20, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
button3.place(x=10, y=170)

button4 = tk.Button(frame_alpr, text="Theft", command=Theft, width=20, height=2,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=250)

button4 = tk.Button(frame_alpr, text="Fraud", command=Fraud,width=20, height=2,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=330)

button5 = tk.Button(frame_alpr, text="Prediction", command=pre, width=20, height=2,bg="white",fg="black", font=('times', 15, ' bold '))
button5.place(x=10, y=420)

#button4 = tk.Button(frame_alpr, text="Wood_sorel", command=Wood_Sorel,width=20, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
#button4.place(x=10, y=430)

exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=2, font=('times', 15, ' bold '),bg="black",fg="white")
exit.place(x=10, y=500)



root.mainloop()

