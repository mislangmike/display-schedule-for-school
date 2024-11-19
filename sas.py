import tkinter as tk
from tkinter import ttk
import time

class AttendanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Tracker")

        # Create labels and entry fields for student names
        self.student_labels = []
        self.student_entries = []
        for i in range(10):  # Adjust the number of students as needed
            label = tk.Label(root, text=f"Student {i+1}:")
            entry = tk.Entry(root)
            label.grid(row=i, column=0)
            entry.grid(row=i, column=1)
            self.student_labels.append(label)
            self.student_entries.append(entry)

        # Create a button to mark attendance
        self.mark_attendance_button = tk.Button(root, text="Mark Attendance", command=self.mark_attendance)
        self.mark_attendance_button.grid(row=11, column=0, columnspan=2)

        # Create a text widget to display the attendance list
        self.attendance_list = tk.Text(root, wrap=tk.WORD, width=40, height=10)
        self.attendance_list.grid(row=12, column=0, columnspan=2)

    def mark_attendance(self):
        attendance_data = []
        for entry in self.student_entries:
            student_name = entry.get()
            if student_name:
                attendance_data.append(student_name)

        # Add a timestamp to the attendance data
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        attendance_data.insert(0, timestamp)

        # Display the attendance list in the text widget
        self.attendance_list.delete(1.0, tk.END)
        for entry in attendance_data:
            self.attendance_list.insert(tk.END, entry + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceTracker(root)
    root.mainloop()