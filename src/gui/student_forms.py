import tkinter as tk
from tkinter import ttk, messagebox
from models.student import Student
from utils.generate_id import generate_id

class StudentListFrame(ttk.Frame):
    def __init__(self, parent, library, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.library = library
        self._create_widgets()
        self._populate_students()

    def _create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Surname", "Email", "Major", "Year"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def _populate_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in self.library.students.values():
            self.tree.insert("", tk.END, values=(
                student.person_id, student.name, student.surname, student.email, student.major, student.year
            ))

class RegisterStudentDialog(tk.Toplevel):
    def __init__(self, parent, library):
        super().__init__(parent)
        self.library = library
        self.title("Register Student")
        self.geometry("350x350")
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        labels = ["Name", "Surname", "Email", "Major", "Year"]
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self, text=label+":").grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry
        ttk.Button(self, text="Register Student", command=self._on_register).grid(row=len(labels), column=0, columnspan=2, pady=15)

    def _on_register(self):
        try:
            name = self.entries["Name"].get().strip()
            surname = self.entries["Surname"].get().strip()
            email = self.entries["Email"].get().strip()
            major = self.entries["Major"].get().strip()
            year = int(self.entries["Year"].get().strip())
            id_ = generate_id(name, surname)
            student = Student(name, surname, id_, email, major, year)
            self.library.register_student(student)
            messagebox.showinfo("Success", f"Student '{name} {surname}' registered. ID: {id_}")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e)) 