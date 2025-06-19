import tkinter as tk
from tkinter import ttk, messagebox
from gui.book_forms import BookListFrame, AddBookDialog
from gui.student_forms import StudentListFrame, RegisterStudentDialog
from gui.dialogs import LibrarianListFrame, RegisterLibrarianDialog, BorrowBookDialog, ReturnBookDialog

class LibraryMainWindow(tk.Tk):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.title(f"Library Management System - {self.library.name}")
        self.geometry("1000x650")
        self._setup_style()
        self._create_status_bar()
        self._create_layout()
        self._show_welcome()

    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Header.TLabel', font=("Arial", 22, "bold"), foreground="#2a4d69", padding=10)
        style.configure('Section.TLabel', font=("Arial", 14, "bold"), foreground="#4b86b4", padding=5)
        style.configure('Sidebar.TButton', font=("Arial", 14, "bold"), padding=12, foreground="#fff", background="#2a4d69")
        style.map('Sidebar.TButton', background=[('active', '#4b86b4')])
        style.configure('TButton', font=("Arial", 12), padding=6)
        style.configure('Treeview.Heading', font=("Arial", 12, "bold"), foreground="#2a4d69")
        style.configure('TLabel', font=("Arial", 12))

    def _clear_main_content(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def _create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Welcome to the Library Management System!")
        status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor='w')
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _create_layout(self):
        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        # Sidebar
        self.sidebar = ttk.Frame(container, width=200, style='Sidebar.TFrame')
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self._create_sidebar_buttons()
        # Main content
        self.main_frame = ttk.Frame(container)
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _create_sidebar_buttons(self):
        buttons = [
            ("Home", self._show_welcome),
            ("Books", self._show_books),
            ("Add Book", self._add_book),
            ("Students", self._show_students),
            ("Register Student", self._register_student),
            ("Librarians", self._show_librarians),
            ("Register Librarian", self._register_librarian),
            ("Borrow Book", self._borrow_book),
            ("Return Book", self._return_book),
            ("Reports", self._generate_report),
            ("Exit", self.quit)
        ]
        for text, command in buttons:
            btn = ttk.Button(self.sidebar, text=text, style='Sidebar.TButton', command=command)
            btn.pack(fill=tk.X, pady=2, padx=10)

    def _show_welcome(self):
        self._clear_main_content()
        ttk.Label(self.main_frame, text="Welcome to", style='Section.TLabel').pack(pady=(40, 0))
        ttk.Label(self.main_frame, text=self.library.name, style='Header.TLabel').pack(pady=(0, 10))
        ttk.Label(self.main_frame, text="A modern, intuitive Library Management System.", style='Section.TLabel').pack(pady=(0, 30))
        ttk.Label(self.main_frame, text="Use the sidebar to manage books, students, librarians, and borrowing operations.", wraplength=700, justify=tk.CENTER).pack(pady=(0, 10))
        self.status_var.set("Ready.")

    def _show_books(self):
        self._clear_main_content()
        ttk.Label(self.main_frame, text="Books", style='Header.TLabel').pack(anchor="w", padx=20, pady=(10, 0))
        frame = BookListFrame(self.main_frame, self.library)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.status_var.set("Viewing books.")

    def _add_book(self):
        def on_close():
            self._show_books()
        dialog = AddBookDialog(self, self.library)
        dialog.protocol("WM_DELETE_WINDOW", lambda: (on_close(), dialog.destroy()))
        dialog.wait_window()
        self._show_books()
        self.status_var.set("Book added.")

    def _show_students(self):
        self._clear_main_content()
        ttk.Label(self.main_frame, text="Students", style='Header.TLabel').pack(anchor="w", padx=20, pady=(10, 0))
        frame = StudentListFrame(self.main_frame, self.library)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.status_var.set("Viewing students.")

    def _register_student(self):
        def on_close():
            self._show_students()
        dialog = RegisterStudentDialog(self, self.library)
        dialog.protocol("WM_DELETE_WINDOW", lambda: (on_close(), dialog.destroy()))
        dialog.wait_window()
        self._show_students()
        self.status_var.set("Student registered.")

    def _show_librarians(self):
        self._clear_main_content()
        ttk.Label(self.main_frame, text="Librarians", style='Header.TLabel').pack(anchor="w", padx=20, pady=(10, 0))
        frame = LibrarianListFrame(self.main_frame, self.library)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.status_var.set("Viewing librarians.")

    def _register_librarian(self):
        def on_close():
            self._show_librarians()
        dialog = RegisterLibrarianDialog(self, self.library)
        dialog.protocol("WM_DELETE_WINDOW", lambda: (on_close(), dialog.destroy()))
        dialog.wait_window()
        self._show_librarians()
        self.status_var.set("Librarian registered.")

    def _borrow_book(self):
        def on_close():
            self._show_books()
        dialog = BorrowBookDialog(self, self.library)
        dialog.protocol("WM_DELETE_WINDOW", lambda: (on_close(), dialog.destroy()))
        dialog.wait_window()
        self._show_books()
        self.status_var.set("Book borrowed.")

    def _return_book(self):
        def on_close():
            self._show_books()
        dialog = ReturnBookDialog(self, self.library)
        dialog.protocol("WM_DELETE_WINDOW", lambda: (on_close(), dialog.destroy()))
        dialog.wait_window()
        self._show_books()
        self.status_var.set("Book returned.")

    def _generate_report(self):
        self._clear_main_content()
        ttk.Label(self.main_frame, text="Library Report", style='Header.TLabel').pack(anchor="w", padx=20, pady=(10, 0))
        report = self.library.generate_report()
        label = ttk.Label(self.main_frame, text=report, font=("Arial", 12), justify=tk.LEFT)
        label.pack(padx=20, pady=20, anchor="nw")
        self.status_var.set("Report generated.") 