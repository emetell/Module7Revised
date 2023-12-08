import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from tkinter import ttk


def load_csv(tree):
    file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)  # Skip the header
                data = [row for row in reader]

            # Calculate average scores
            for row in data:
                scores = list(map(int, row[1:]))
                average = round(sum(scores) / len(scores), 2)
                row.append(average)

            # Sort students by average scores in descending order
            data_sorted = sorted(data, key=lambda x: x[-1], reverse=True)

            # Display sorted data in Treeview
            display_data(tree, data_sorted)

        except FileNotFoundError:
            messagebox.showinfo("Error", "File not found.")
        except Exception as e:
            messagebox.showinfo("Error", f"An error occurred: {e}")

def display_data(tree, data):
    # Clear existing data
    for item in tree.get_children():
        tree.delete(item)

    # Insert new data into Treeview
    for i, row in enumerate(data):
        tree.insert("", "end", values=row)  # Specify the column indices

def export_csv(tree):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if file_path:
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write header
                header = ["Name", "Average"]
                writer.writerow(header)

                # Write data
                for row in tree.get_children():
                    values = tree.item(row, 'values')
                    newrow = [values[0], values[-1]]
                    writer.writerow(newrow)

            messagebox.showinfo("Export", f"Data exported to {file_path}")

        except Exception as e:
            messagebox.showinfo("Error", f"An error occurred: {e}")
