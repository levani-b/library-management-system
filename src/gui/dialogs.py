import tkinter as tk
from tkinter import ttk, messagebox
from models.librarian import Librarian, AccessLevel
from models.student import Student
from models.book import Book
from datetime import date, timedelta
from utils.generate_id import generate_id

class LibrarianListFrame(ttk.Frame):
    def __init__(self, parent, library, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.library = library
        self._create_widgets()
        self._populate_librarians()

    def _create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Surname", "Email", "Access Level"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def _populate_librarians(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for librarian in self.library.librarians.values():
            self.tree.insert("", tk.END, values=(
                librarian.person_id, librarian.name, librarian.surname, librarian.email, librarian.access_level
            ))

class RegisterLibrarianDialog(tk.Toplevel):
    def __init__(self, parent, library):
        super().__init__(parent)
        self.library = library
        self.title("Register Librarian")
        self.geometry("350x350")
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        labels = ["Name", "Surname", "Email", "Access Level"]
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self, text=label+":").grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            if label == "Access Level":
                combo = ttk.Combobox(self, values=[level.value for level in AccessLevel], state="readonly")
                combo.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label] = combo
            else:
                entry = ttk.Entry(self)
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label] = entry
        ttk.Button(self, text="Register Librarian", command=self._on_register).grid(row=len(labels), column=0, columnspan=2, pady=15)

    def _on_register(self):
        try:
            name = self.entries["Name"].get().strip()
            surname = self.entries["Surname"].get().strip()
            email = self.entries["Email"].get().strip()
            access_level = self.entries["Access Level"].get().strip()
            id_ = generate_id(name, surname)
            librarian = Librarian(name, surname, id_, email, access_level)
            self.library.register_librarian(librarian)
            messagebox.showinfo("Success", f"Librarian '{name} {surname}' registered. ID: {id_}")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

class BorrowBookDialog(tk.Toplevel):
    def __init__(self, parent, library):
        super().__init__(parent)
        self.library = library
        self.title("Borrow Book")
        self.geometry("400x250")
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Select Student:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.student_var = tk.StringVar()
        student_choices = [f"{s.name} {s.surname} ({s.person_id})" for s in self.library.students.values()]
        self.student_combo = ttk.Combobox(self, values=student_choices, textvariable=self.student_var, state="readonly")
        self.student_combo.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self, text="Select Book:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.book_var = tk.StringVar()
        available_books = [b for b in self.library.books.values() if b.is_available()]
        book_choices = [f"{b.title} by {b.author} ({b.isbn})" for b in available_books]
        self.book_combo = ttk.Combobox(self, values=book_choices, textvariable=self.book_var, state="readonly")
        self.book_combo.grid(row=1, column=1, padx=10, pady=5)

        # Borrow days
        ttk.Label(self, text="Borrow Days:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.days_entry = ttk.Entry(self)
        self.days_entry.insert(0, "14")
        self.days_entry.grid(row=2, column=1, padx=10, pady=5)
        ttk.Button(self, text="Borrow", command=self._on_borrow).grid(row=3, column=0, columnspan=2, pady=15)

    def _on_borrow(self):
        try:
            student_display = self.student_var.get()
            book_display = self.book_var.get()
            if not student_display or not book_display:
                raise ValueError("Please select both a student and a book.")
            student_id = student_display.split('(')[-1].rstrip(')')
            isbn = book_display.split('(')[-1].rstrip(')')
            days = int(self.days_entry.get().strip())
            borrow_date = date.today()
            due_date = borrow_date + timedelta(days=days)
            self.library.borrow_book(student_id, isbn, borrow_date, due_date)
            messagebox.showinfo("Success", f"Book borrowed until {due_date}.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

class ReturnBookDialog(tk.Toplevel):
    def __init__(self, parent, library):
        super().__init__(parent)
        self.library = library
        self.title("Return Book")
        self.geometry("400x200")
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Select Student:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.student_var = tk.StringVar()
        student_choices = [f"{s.name} {s.surname} ({s.person_id})" for s in self.library.students.values()]
        self.student_combo = ttk.Combobox(self, values=student_choices, textvariable=self.student_var, state="readonly")
        self.student_combo.grid(row=0, column=1, padx=10, pady=5)
        self.student_combo.bind("<<ComboboxSelected>>", self._update_books)

        ttk.Label(self, text="Select Book:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.book_var = tk.StringVar()
        self.book_combo = ttk.Combobox(self, values=[], textvariable=self.book_var, state="readonly")
        self.book_combo.grid(row=1, column=1, padx=10, pady=5)

        ttk.Button(self, text="Return", command=self._on_return).grid(row=2, column=0, columnspan=2, pady=15)

    def _update_books(self, event=None):
        student_display = self.student_var.get()
        if not student_display:
            self.book_combo['values'] = []
            return
        student_id = student_display.split('(')[-1].rstrip(')')
        student = self.library.students.get(student_id)
        if not student:
            self.book_combo['values'] = []
            return
        borrowed_books = student.borrowed_books
        book_choices = [f"{b.title} by {b.author} ({b.isbn})" for b in borrowed_books]
        self.book_combo['values'] = book_choices
        if book_choices:
            self.book_combo.current(0)
        else:
            self.book_var.set("")

    def _on_return(self):
        try:
            student_display = self.student_var.get()
            book_display = self.book_var.get()
            if not student_display or not book_display:
                raise ValueError("Please select both a student and a book.")
            student_id = student_display.split('(')[-1].rstrip(')')
            isbn = book_display.split('(')[-1].rstrip(')')
            return_date = date.today()
            self.library.return_book(student_id, isbn, return_date)
            messagebox.showinfo("Success", f"Book returned on {return_date}.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e)) 