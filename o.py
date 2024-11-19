import tkinter as tk
from tkinter import filedialog
import csv
import os

# Function to handle student submission
def submit_attendance(name, attendance_status, proof_image_path):
    try:
        # Validate proof image
        if not proof_image_path or not os.path.isfile(proof_image_path):
            raise ValueError("Please select a valid proof image.")

        # Store data in a CSV file (adjust as needed)
        with open('attendance_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['Name', 'Attendance', 'Proof']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Name': name, 'Attendance': attendance_status, 'Proof': proof_image_path})

        # Display a success message
        success_label.config(text="Attendance submitted successfully!")
    except Exception as e:
        # Handle potential errors
        error_label.config(text=f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Student Attendance")

# Labels and input fields
name_label = tk.Label(window, text="Hello, \"Cabagua, Mike Lorenz, M.\"")
name_label.pack()

attendance_label = tk.Label(window, text="Attendance:")
attendance_label.pack()

present_button = tk.Radiobutton(window, text="Present")
present_button.pack()
excuse_button = tk.Radiobutton(window, text="Excuse")
excuse_button.pack()

proof_label = tk.Label(window, text="Proof:")
proof_label.pack()

proof_entry = tk.Entry(window)
proof_entry.pack()

# Browse button for proof image
browse_button = tk.Button(window, text="Browse", command=lambda: browse_file())
browse_button.pack()

# Success and error message labels
success_label = tk.Label(window, text="")
success_label.pack()
error_label = tk.Label(window, text="", fg="red")
error_label.pack()

# Submit button
submit_button = tk.Button(window, text="Submit", command=lambda: submit_attendance(name_label.get(), present_button.get(), proof_entry.get()))
submit_button.pack()

# Function to browse for a proof image file
def browse_file():
    file_path = filedialog.askopenfilename()
    proof_entry.delete(0, tk.END)
    proof_entry.insert(0, file_path)

# Run the application
window.mainloop()