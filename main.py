import tkinter as tk

from tkinter import ttk
from app.functions import load_csv, export_csv

def main():
    root = tk.Tk()
    root.title("Student Average Scores")

    load_button = tk.Button(root, text="Load CSV", command=lambda: load_csv(tree))
    load_button.pack(pady=10)

    export_button = tk.Button(root, text="Export CSV", command=lambda: export_csv(tree))
    export_button.pack(pady=10)

    tree = ttk.Treeview(root)
    tree["columns"] = ("Name", "Math", "English", "History", "Average")
    tree.heading("#0", text="")
    tree.column("#0", anchor="center", width=2)  # Center the data

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=80)  # Center the data

    tree.pack(expand=tk.YES, fill=tk.BOTH)

    root.mainloop()

if __name__ == "__main__":
    main()
