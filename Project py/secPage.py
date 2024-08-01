from tkinter import *
from tkinter import messagebox
secPage = Tk()
secPage.title("STUDENT INFO")
secPage.geometry("1600x900")


#--------frames-------------#
whole_frame=Frame(secPage,bg= '#E2DAD6')
whole_frame.place(width=1600,height=900)

main_frame=Frame(secPage , bg= '#E2DAD6')
main_frame.place(relx=0.5,rely=0.5,anchor='center')

#-----------------------------------------------------

adge_frame = Frame(secPage , bg= '#6482AD')
adge_frame.place(x=0 , y= 0 , width=1600 , height=95)

#-----------------------------------------------------

title_frame = Frame(secPage , bg= '#7FA1C3')
title_frame.place(x=0 , y= 98 , width=1600 , height=100)

#-----------------------------------------------------

#-------font----------------#

baseFont = ('Tahoma' , 20)

#-----------------------------------------------------

#--------showing title-----#

title_lbl = Label(title_frame,text= 'Department Classification System',font= baseFont,bg= '#7FA1C3',justify='center', fg='white')
title_lbl.pack(pady=20)

title_adge_frame_lbl = Label(adge_frame,text = 'College of Computer Science and Artificial Intelligence',font = baseFont,justify = 'center',fg= 'white',bg='#6482AD')
title_adge_frame_lbl.pack(pady=20)

#-----------------------------------------------------

#---------labels&Entries---#

lbl1=Label(main_frame,text="Student Info",fg="black",font=baseFont,justify='center' ,bg= '#E2DAD6')   #---->page title

lbl1.grid(row=0,columnspan=4,pady=50)
#----------------------------------------------------

lbl_name=Label(main_frame,text="Name",fg="black",font=baseFont ,bg= '#E2DAD6')      #---->Name
txt_name=Entry(main_frame,font=baseFont )

lbl_name.grid(row=1,column=2,padx=50,pady=2)
txt_name.grid(row=1,column=3)

#-----------------------------------------------------

lbl_studentId=Label(main_frame,text="Student Id",fg="black",font=baseFont,bg= '#E2DAD6') #---->Student ID
txt_studentId=Entry(main_frame,font=baseFont)

lbl_studentId.grid(row=2,column=2,padx=50,pady=2)
txt_studentId.grid(row=2,column=3)

#-----------------------------------------------------

lbl_studentCode=Label(main_frame,text="Student Code",fg="black",font=baseFont ,bg= '#E2DAD6')     #---->Student Code
txt_studentCode=Entry(main_frame,font=baseFont)

lbl_studentCode.grid(row=3,column=2,padx=50,pady=2)
txt_studentCode.grid(row=3,column=3)

#-----------------------------------------------------

lbl_academic=Label(main_frame,text="Academic Year",fg="black",font=baseFont ,bg= '#E2DAD6')    #---->Year
txt_year=Entry(main_frame,font=baseFont)

lbl_academic.grid(row=4,column=2,padx=50,pady=2)
txt_year.grid(row=4,column=3)

#-----------------------------------------------------

lbl_hours=Label(main_frame,text="Passed Hours",fg="black",font=baseFont ,bg= '#E2DAD6')     #---->Hours
txt_hours=Entry(main_frame,font=baseFont)

lbl_hours.grid(row=5,column=2,padx=50,pady=2)
txt_hours.grid(row=5,column=3)

#-----------------------------------------------------

lbl_gpa=Label(main_frame,text="GPA",fg="black",font=baseFont ,bg= '#E2DAD6')    #---->GPA
txt_gpa=Entry(main_frame,font=baseFont)

lbl_gpa.grid(row=6,column=2,padx=50,pady=2)
txt_gpa.grid(row=6,column=3)
#-----------------------------------------------------

regis_btn=Button(main_frame,text="Register",width=20,font=("Arial", 14), bg="#6482AD" , fg='white')   #----> register button

regis_btn.grid(row=7,column=2,pady=50,padx=30)

#-----------------------------------------------------

abt_btn=Button(main_frame,text="About",width=20,font=("Arial", 14), bg="#6482AD" , fg='white')   #-----> About button

abt_btn.grid(row=7,column=3)
#-----------------------------------------------------

secPage.mainloop()