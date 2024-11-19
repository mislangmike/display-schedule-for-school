import tkinter as tk
import csv

# Function to handle student submission
def submit_attendance(name, attendance_status, proof_image):
    # Replace with your desired data storage method
    with open('attendance_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Attendance', 'Proof']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Attendance': attendance_status, 'Proof': proof_image})

# Create the main window
window = tk.Tk()
window.title("Student Attendance")

# Labels and input fields
name_label = tk.Label(window, text="Hello, \"Surname, Name, Middle initials\"")
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

# Submit button
submit_button = tk.Button(window, text="Submit", command=lambda: submit_attendance("Cabagua, Mike Lorenz, M.".get(), present_button.get(), proof_entry.get()))
submit_button.pack()

# Run the application
window.mainloop()