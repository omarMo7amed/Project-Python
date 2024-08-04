import tkinter as tk
from tkinter import scrolledtext
import subprocess

import registerDepartment


class Thied(tk.Tk):
    def __init__(self, stu_Id="",stu_code=""):
        super().__init__()
        self.stu_Id = stu_Id
        self.stu_code = stu_code
        self.title("About")
        self.geometry('1200x600+100+100')
        self.configure(bg="#438BB1")
        self.create_widgets()

    def back(self):
        self.destroy()  # Destroy the current window
        registerDepartment.transition_registerDepartment(self.stu_code,self.stu_Id)  # Run the other script

    def create_widgets(self):
        # Main Frame
        frame = tk.Frame(self, bg="#438BB1")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Labels
        label2 = tk.Label(frame, text="AI", font=("Segoe UI Semibold", 22), bg="#438BB1", anchor="center")
        label3 = tk.Label(frame, text="SC", font=("Segoe UI Semibold", 22), bg="#438BB1", anchor="center")
        label4 = tk.Label(frame, text="IS", font=("Segoe UI Semibold", 22), bg="#438BB1", anchor="center")
        label5 = tk.Label(frame, text="CS", font=("Segoe UI Semibold", 22), bg="#438BB1", anchor="center")

        # Text Areas
        text_area2 = scrolledtext.ScrolledText(frame, width=50, height=10, wrap=tk.WORD)
        text_area2.insert(tk.END, "The Scientific Computing department focuses on developing and introducing new computational methods for educational and scientific research by leveraging rapidly evolving and high-performance computing technology...")
        text_area2.config(state=tk.DISABLED)

        text_area3 = scrolledtext.ScrolledText(frame, width=50, height=10, wrap=tk.WORD)
        text_area3.insert(tk.END, "The primary interest of the Computer Science department is to understand, develop, and advance the scientific concepts behind what computers accomplish and how they achieve it, including the knowledge of computer architecture and operation...")
        text_area3.config(state=tk.DISABLED)

        text_area4 = scrolledtext.ScrolledText(frame, width=50, height=10, wrap=tk.WORD)
        text_area4.insert(tk.END, "The main focus of the Information Systems department is to study all technical issues, high-level management issues, and policy planning associated with employing computers to create information systems for organizations and institutions...")
        text_area4.config(state=tk.DISABLED)

        text_area5 = scrolledtext.ScrolledText(frame, width=50, height=10, wrap=tk.WORD)
        text_area5.insert(tk.END, "The main focus of the Artificial Intelligence department is to study and simulate the human mind, understand its nature and how it works, such as its ability to think, discover, and learn from past experiences...")
        text_area5.config(state=tk.DISABLED)

        # Back Button
        back_button = tk.Button(frame, text="Back", font=("Segoe UI", 12), bg="#D1B87F", command=self.back)

        # Layout
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        label3.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        label5.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        text_area2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        text_area3.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        label4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        label2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        text_area4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        text_area5.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        back_button.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="e")

class SecondPage(tk.Tk):
    def __init__(self, stu_I):
        super().__init__()
        self.stu_I = stu_I
        self.title("Second Page")
        self.geometry("400x300")
        label = tk.Label(self, text=f"Welcome, {self.stu_I}", font=("Segoe UI", 18))
        label.pack(pady=20)
        back_button = tk.Button(self, text="Back", font=("Segoe UI", 12), command=self.back_action)
        back_button.pack(pady=20)

    def back_action(self):
        self.destroy()
        Thied().mainloop()

if __name__ == "__main__":
    app = Thied()
    app.mainloop()
