import tkinter as tk
from tkinter import ttk, messagebox
from models.book import Book

class BookListFrame(ttk.Frame):
    def __init__(self, parent, library, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.library = library
        self._create_widgets()
        self._populate_books()

    def _create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ISBN", "Title", "Author", "Genre", "Year", "Available", "Total"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def _populate_books(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in self.library.books.values():
            self.tree.insert("", tk.END, values=(
                book.isbn, book.title, book.author, book.genre, book.publication_year, book.copies_available, book.total_copies
            ))

class AddBookDialog(tk.Toplevel):
    def __init__(self, parent, library):
        super().__init__(parent)
        self.library = library
        self.title("Add Book")
        self.geometry("350x350")
        self.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        labels = ["Title", "Author", "ISBN", "Genre", "Publication Year", "Copies Available", "Total Copies"]
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self, text=label+":").grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry
        ttk.Button(self, text="Add Book", command=self._on_add).grid(row=len(labels), column=0, columnspan=2, pady=15)

    def _on_add(self):
        try:
            title = self.entries["Title"].get().strip()
            author = self.entries["Author"].get().strip()
            isbn = self.entries["ISBN"].get().strip()
            genre = self.entries["Genre"].get().strip()
            year = int(self.entries["Publication Year"].get().strip())
            copies_available = int(self.entries["Copies Available"].get().strip())
            total_copies = int(self.entries["Total Copies"].get().strip())
            book = Book(title, author, isbn, genre, year, copies_available, total_copies)
            self.library.add_book(book)
            messagebox.showinfo("Success", f"Book '{title}' added.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e)) 