from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image , ImageTk
import sqlite3
import secPage


# student_code :'202233235',  student id:'30402051700999' //test
  #==> login window
root = Tk()
root.iconbitmap("images\\icon1.ico")
root.resizable('false' , 'false')

# ---------------- Images --------------------------
photo = Image.open('images\\stu2.png')
image_tk = ImageTk.PhotoImage(photo)

photo2 = Image.open('images\\FCI_Logo3.png')
image_tk2 = ImageTk.PhotoImage(photo2)

#img2 = photo2.resize(((101, 107)))
#img2.save('images\FCI_Logo3.png')



# Functions
def setShowId():
    if show_student_id_var.get():
        show_student_id_var.set(1);
        student_id_entry.config(show="")  # Show text
    else:
        show_student_id_var.set(0)
        student_id_entry.config(show="*")  # Hide text with *
# ------------------ fonts  ------------------
baseFont = ('Tahoma' , 20)


# ------------------ frames ------------------

adge_frame = Frame(root , bg= '#6482AD')
adge_frame.place(x=0 , y= 0 , width=1200 , height=95)

title_frame = Frame(root , bg= '#7FA1C3')
title_frame.place(x=0 , y= 98 , width=1200 , height=100)

login_frame = Frame(root , background = '#E2DAD6')
login_frame.place(x=380 , y=210 , width=800 , height=350 )

photo_frame = Frame(root , background = 'silver')
photo_frame.place(x=20 , y=210 , width=340 , height=350 )

# ------------------ lablels and Entry ------------------

title_lbl = Label(title_frame ,
                  text = 'Department Classification System' , 
                  font = baseFont , 
                  bg= '#7FA1C3' ,
                  justify='center' , 
                  fg='white')
title_lbl.pack(pady=20)


photo_fci_label = Label(adge_frame, image=image_tk2 , padx=5)
photo_fci_label.pack(side='left')

title_adge_frame_lbl = Label(adge_frame ,
                             text = 'College of Computer Science and Artificial Intelligence' , 
                             font = baseFont , 
                             justify = 'center' ,
                             fg= 'white' ,
                             bg='#6482AD')
title_adge_frame_lbl.pack(pady=20)


student_id_lbl = Label(login_frame,
                        text="Student Id", 
                        font = ("Arial",16) ,
                        justify='center' ,
                        bg='#E2DAD6')
student_id_lbl.grid(row = 2 , column = 0 , pady = 20 , padx = 20)

student_id_entry = Entry(login_frame, font = baseFont,show='*')
student_id_entry.grid(row = 2 , column = 1, pady = 20)


student_code_label = Label(login_frame,
                           text="Student code", 
                           font = ("Arial",16) ,
                           justify='center' ,
                           bg='#E2DAD6')
student_code_label.grid(row = 1 , column = 0 , pady = 60 , padx = 100)

student_code_entry = Entry(login_frame, font = baseFont)
student_code_entry.grid(row = 1 , column = 1, pady = 20)


def handleSubmit():
    student_code = student_code_entry.get()
    student_id=student_id_entry.get()

    # check if empty or not
    if not student_code:
        print("Student Code is required.")
        return
    if not student_id:
        print("Student ID is required.")
        return
    
     # Connect to the database
    conn = sqlite3.connect('./data/college_registration.db',)
    cursor = conn.cursor()

    # Check if student_id and student_code exist in the database
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    result_id = cursor.fetchone()
    
    cursor.execute("SELECT * FROM students WHERE student_code = ?", (student_code,))
    result_code = cursor.fetchone()
    
    
    if result_code is None:
        messagebox.showerror("Error", "Enter valid code")
        return
        
    if result_id is None:
        messagebox.showerror("Error", "Your id Not valid")
        return
    
    
    #Hello message
    cursor.execute("SELECT name FROM students WHERE student_code = ?", (student_code,))
    result_name = cursor.fetchone()
    messagebox.showinfo('Valid', f"Welcome, {result_name[0]}")
    
    #Navigate page
    global id
    global code
    id=student_id_entry.get()
    code=student_code_entry.get()
    root.destroy()
    secPage.transition(code,id)
    cursor.close()
    conn.close()
    

photo_main_label = Label(photo_frame, image=image_tk)
photo_main_label.pack()


# --------------- Checkbox ------------------

show_student_id_var = IntVar()
show_student_id_var.set(0)


show_student_id_checkbox = Checkbutton(login_frame,
                                        text = "Show ID", 
                                        variable = show_student_id_var, 
                                        bg = "#6482AD", 
                                        command = setShowId ,
                                       )

show_student_id_checkbox.grid(row=3, column=1, pady=5 , sticky='e')

# --------------- Submit button --------------- 

submit_button = Button(login_frame, text="Login", font=("Arial", 14), bg="#6482AD" , fg='white',command=handleSubmit)
submit_button.grid(row=4, column=1 , pady=(20, 0) , sticky='w')

root.title('LOGIN')
root.geometry('1200x600+100+100')
root.mainloop()
