from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import getInfo
import about

departmentSelected=[]

departmentGpa = {"Computer Science": 3.2,  "Artificial Intelligence":3, "Information Systems":2.6, "Scientific Computing":1}

def transition_registerDepartment(code, id):
    # Initialize the main window
    registerDepartment = Tk()
    registerDepartment.title("DEPARTMENTS REGISTRATION")
    registerDepartment.geometry("1200x600+100+100")

    def Back():
        registerDepartment.destroy()
        getInfo.transition(code, id)

    def About():
        registerDepartment.destroy()
        about.Thied(id, code)

    # Connect to the database
    conn = sqlite3.connect('./data/college_registration.db',)
    cursor = conn.cursor()

    # Frames
    whole_frame = Frame(registerDepartment, bg='#E2DAD6')
    whole_frame.place(width=1200, height=600)

    main_frame = Frame(registerDepartment, bg='#E2DAD6')
    main_frame.place(relx=0.5, rely=0.55, anchor='center')  # Adjusted relx and rely for centering

    adge_frame = Frame(registerDepartment, bg='#6482AD')
    adge_frame.place(x=0, y=0, width=1200, height=70)  # Adjusted height

    title_frame = Frame(registerDepartment, bg='#7FA1C3')
    title_frame.place(x=0, y=73, width=1200, height=80)  # Adjusted y and height

    # Fonts
    baseFont = ('Tahoma', 16)  # Adjusted font size

    # Titles
    title_lbl = Label(title_frame, text='Department Classification', font=baseFont, bg='#7FA1C3', justify='center', fg='white')
    title_lbl.pack(pady=10)  # Adjusted pady

    title_adge_frame_lbl = Label(adge_frame, text='College of Computer Science and Artificial Intelligence', font=baseFont, justify='center', fg='white', bg='#6482AD')
    title_adge_frame_lbl.pack(pady=10)  # Adjusted pady

    # Labels and ComboBoxes
    departments = ["Computer Science", "Information Systems", "Artificial Intelligence", "Scientific Computing"]
    comboboxes = []

    def update_comboboxes(event):
        department_selected = [cb.get() for cb in comboboxes if cb.get() != '']

        # Push data into departmentSelected
        data = event.widget
        value = data.get()
        departmentSelected.append(value)

        for cb in comboboxes:
            current_value = cb.get()
            if current_value:
                available_departments = [d for d in departments if d not in department_selected or d == current_value]
            else:
                available_departments = [d for d in departments if d not in department_selected]
            cb['values'] = available_departments

    def createComboBox(text, numRow):
        lbl = Label(main_frame, text=text, fg="black", font=baseFont, bg='#E2DAD6')
        lbl.grid(row=numRow, column=0, padx=20, pady=10)  # Adjusted padx for labels
        compo_box = ttk.Combobox(main_frame, values=departments, font=baseFont, width=30)  # Increased width
        compo_box.grid(row=numRow, column=1, padx=20, pady=10)  # Adjusted padx for ComboBoxes
        compo_box.bind("<<ComboboxSelected>>", update_comboboxes)
        comboboxes.append(compo_box)

    createComboBox('Department 1', 0)
    createComboBox('Department 2', 1)
    createComboBox('Department 3', 2)
    createComboBox('Department 4', 3)

    def specifyDepartment(studentGpa):
         validDepartment = []
        #  get valid department depend on your gpa 
         for dp_name, dp_gpa in departmentGpa.items():
             if studentGpa >= dp_gpa:
                 validDepartment.append(dp_name)
        
         print(validDepartment)
         print(departmentSelected)
        
         def get_index_safe(lst, element):
            try:
                 return lst.index(element)
            except ValueError:
                 return None


        #  get validDepartment depend on departmentSelected
         for i in range(4):
             index = get_index_safe(validDepartment,departmentSelected[i])
             if type(index) is int:
                 cursor.execute("select department_id from departments where department_name=?",(validDepartment[index],))
                 [department_ID]=cursor.fetchone()
                 cursor.execute("UPDATE students SET department_id =? WHERE student_id=?", (department_ID,id,))
                 conn.commit()
                 messagebox.showinfo('Success', f"Congratulations, You Joined to {validDepartment[index]} Department")
                 return
             
         messagebox.showerror("Error", "Sorry, not allowed to register department (your GPA under 1.0)")

    def handleSubmit():
       cursor.execute("SELECT gpa,department_id FROM students WHERE student_id = ?", (id,))
       [gpa,department_id] = cursor.fetchone()
       
       #handle you have to fill all comboBox
       if len(departmentSelected) < 4:
           return messagebox.showerror("Error", "Choose all departments")
       
       cursor.execute("SELECT department_name FROM departments WHERE department_id = ?", (department_id,))
       department_name = cursor.fetchone()
       print(department_name)
       
       #handle if you already joined to department
       if department_id:
           return messagebox.showerror("Error", f"You already in {department_name[0]}")
       
       
       #The first time to register
       specifyDepartment(gpa)
       return

    # Buttons
    about_btn = Button(main_frame, text="About", width=15, font=("Arial", 12), bg="#6482AD", fg='white', command=About)  # Adjusted width and font size
    about_btn.grid(row=5, column=0, pady=30, padx=20)

    registration_btn = Button(main_frame, text="Register", width=15, font=("Arial", 12), bg="#6482AD", fg='white', command=handleSubmit)  # Adjusted width and font size
    registration_btn.grid(row=5, column=1, pady=30, padx=20)

    back_btn = Button(main_frame, text="Back", width=15, font=("Arial", 12), bg="#6482AD", fg='white', command=Back)  # Adjusted width and font size
    back_btn.grid(row=5, column=2, pady=30, padx=20)

    # Main loop
    registerDepartment.mainloop()
