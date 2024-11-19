import tkinter as tk
import os
import pickle
import random
from datetime import datetime, timedelta
import tkinter as tkk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for Treeview
 
class firstWindow:
 
    def __init__(self):
        self.root = tk.Tk()
        self.load_data()
        self.root.geometry("700x400")
        self.root.resizable(0, 0)
        self.root.title("Schedule System Organizer")
        self.button_student = tk.Button(self.root,
                                        text="Student",
                                        font=('Arial', 16),
                                        command=self.show_studentWindow)
        self.button_student.place(x=300, y=100, width=100)
        self.button_teacher = tk.Button(self.root,
                                        text="Teacher",
                                        font=('Arial', 16),
                                        command=self.show_teacherWindow)
        self.button_teacher.place(x=300, y=150, width=100)
        self.button_admin = tk.Button(self.root,
                                       text="Admin",
                                       font=('Arial', 16),
                                       command=self.show_adminpassWindow)
                                    #    command=self.show_adminWindow)
        self.button_admin.place(x=300, y=200, width=100)
        self.root.protocol("WM_DELETE_WINDOW",
                          self.on_closing)  # Handle window close event
        self.root.mainloop()
 
    def show_studentWindow(self):
        """Displays the student registration window."""
        self.root.withdraw()  # Hide main window
        self.student_root = tk.Toplevel(
            self.root)  # Use Toplevel window
        self.student_root.geometry("400x400")
        self.student_root.resizable(0, 0)
        self.student_root.title("Student Registration")
        self.register_student(self.student_root)  # Call register_student
 
    def register_student(self, student_root):
        """Handles the student registration process."""
 
        # First Name
        self.student_labelFN = tk.Label(student_root,
                                        text="First Name:",
                                        font=('Arial', 12))
        self.student_labelFN.grid(row=0, column=0, padx=10, pady=10)
        self.student_entryFN = tk.Entry(student_root)
        self.student_entryFN.grid(row=0, column=1, padx=10, pady=10)
 
        # Middle Name
        self.student_labelMN = tk.Label(student_root,
                                        text="Middle Name:",
                                        font=('Arial', 12))
        self.student_labelMN.grid(row=1, column=0, padx=10, pady=10)
        self.student_entryMN = tk.Entry(student_root)
        self.student_entryMN.grid(row=1, column=1, padx=10, pady=10)
 
        # Last Name
        self.student_labelLN = tk.Label(student_root,
                                        text="Last Name:",
                                        font=('Arial', 12))
        self.student_labelLN.grid(row=2, column=0, padx=10, pady=10)
        self.student_entryLN = tk.Entry(student_root)
        self.student_entryLN.grid(row=2, column=1, padx=10, pady=10)
 
        # Grade Level Dropdown
        self.grade_options = [
            "Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4",
            "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10",
            "Grade 11", "Grade 12"
        ]
        self.clicked_grade = tk.StringVar(student_root)
        self.clicked_grade.set(self.grade_options[0])
        self.drop = tk.OptionMenu(student_root, self.clicked_grade,
                                  *self.grade_options,
                                  command=self.check_grade)
        self.drop.grid(row=3, column=0, padx=10, pady=10)
 
        # Submit Button
        self.student_button = tk.Button(
            student_root,
            text="Submit",
            font=('Arial', 13),
            command=lambda: self.store_studentData(student_root))
        self.student_button.grid(row=5, column=1, padx=10, pady=10)
 
        # Back Button
        self.back_button = tk.Button(student_root,
                                       text="Back",
                                       font=('Arial', 13),
                                       command=self.back_to_main)
        self.back_button.grid(row=6, column=1, padx=10, pady=10)
 
        self.student_root.protocol("WM_DELETE_WINDOW",
                                   self.on_closing_student)
 
    def check_grade(self, value):
        """
        Checks the selected grade level and displays the strand selection menu if
        the grade is 11 or 12.
        """
        if hasattr(self, 'strand_menu'):
            self.strand_menu.grid_forget()
 
        if value in ["Grade 11", "Grade 12"]:
            self.strand_options = [
                "ABM", "STEM", "HUMSS", "GAS", "ICT"
            ]
            self.clicked_strand = tk.StringVar(self.student_root)
            self.clicked_strand.set(self.strand_options[0])
            self.strand_menu = tk.OptionMenu(self.student_root,
                                             self.clicked_strand,
                                             *self.strand_options)
            self.strand_menu.grid(row=3, column=1, padx=10, pady=10)
        else:
            self.clicked_strand = None
 
    def store_studentData(self, student_root):  # Add student_root as argument
        """Stores student data and validates input."""
        first_name = self.student_entryFN.get().strip().title()
        middle_name = self.student_entryMN.get().strip().title()
        last_name = self.student_entryLN.get().strip().title()
        grade = self.clicked_grade.get()
        strand = self.clicked_strand.get() if grade in ["Grade 11", "Grade 12"] else None
 
        if not all([first_name, last_name, grade]):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
 
        if not first_name.replace(" ", "").isalpha() or not last_name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Names should only contain letters and spaces.")
            return
 
        # Initialize student data with an empty schedule dictionary
        student_data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'grade': grade,
            'section': None,
            'strand': strand,
            'date_issued': self.get_current_date(),
            'schedule': None  # Initialize with None or empty dictionary
        }
 
        if not any(s['first_name'] == first_name
           and s['middle_name'] == middle_name
           and s['last_name'] == last_name for s in self.students):
   
   
         # Add new student if not already in self.students
            self.students.append(student_data)
            self.save_data()
            messagebox.showinfo("Success", "Student added successfully!")
            self.student_root.destroy()  # Close student_root after successful submission
           
            # Initially pass schedule=None when adding a new student
            self.show_studentPOV(first_name, middle_name, last_name, grade, student_data['section'],
                                strand, student_data['date_issued'], student_data['schedule'])
        else:
            # Retrieve the existing student from self.students
            existing_student = next(s for s in self.students
                                    if s['first_name'] == first_name
                                    and s['middle_name'] == middle_name
                                    and s['last_name'] == last_name)
                       
            # Pass the existing student data to show_studentPOV
            self.show_studentPOV(existing_student['first_name'],
                                existing_student['middle_name'],
                                existing_student['last_name'],
                                existing_student['grade'],
                                existing_student['section'],
                                existing_student['strand'],
                                existing_student['date_issued'],
                                existing_student['schedule'])
 
    def show_studentPOV(self, first_name, middle_name, last_name, grade, section,
                    strand, date_issued, schedule):
        """Displays the student point of view window."""
        self.stdPOV_root = tk.Toplevel(self.root)  # Use Toplevel
        self.stdPOV_root.geometry("800x450")
        self.stdPOV_root.resizable(0, 0)
        self.stdPOV_root.title("Schedule System Organizer: Student")
        title_font = ('Arial', 12, 'bold')
        detail_font = ('Arial', 12)
 
        # Start with row 0 and increment it dynamically
        current_row = 0
 
        # Student information
        self.header_label = tk.Label(self.stdPOV_root, text="First Name, Last Name", font=title_font)
        self.header_label.grid(row=current_row, column=0, padx=20, pady=10)
        self.name_label = tk.Label(self.stdPOV_root, text=f"{first_name} {middle_name} {last_name}", font=detail_font)
        self.name_label.grid(row=current_row, column=1, padx=20, pady=10)
 
        # Move to the next row
        current_row += 1
 
        self.grade_label = tk.Label(self.stdPOV_root, text="Grade Level", font=title_font)
        self.grade_label.grid(row=current_row, column=0, padx=20, pady=10)
        self.grade_detail_label = tk.Label(self.stdPOV_root, text=grade, font=detail_font)
        self.grade_detail_label.grid(row=current_row, column=1, padx=20, pady=10)
 
        # Move to the next row
        current_row += 1
 
        # Conditionally display the section if provided
        if section:
            self.section_label = tk.Label(self.stdPOV_root, text="Section", font=title_font)
            self.section_label.grid(row=current_row, column=0, padx=20, pady=10)
            self.section_detail_label = tk.Label(self.stdPOV_root, text=section, font=detail_font)
            self.section_detail_label.grid(row=current_row, column=1, padx=20, pady=10)
 
            # Move to the next row if section is displayed
            current_row += 1
 
        # Conditionally display the strand for Grade 11 and 12
        if grade in ["Grade 11", "Grade 12"] and strand:
            self.strand_label = tk.Label(self.stdPOV_root, text=f"Strand: {strand}", font=detail_font)
            self.strand_label.grid(row=current_row, column=1, padx=20, pady=10)
 
            # Move to the next row if strand is displayed
            current_row += 1
 
        # Display the school year
        self.year_label = tk.Label(self.stdPOV_root, text="School Year", font=title_font)
        self.year_label.grid(row=current_row, column=0, padx=20, pady=10)
        school_year_label = tk.Label(self.stdPOV_root, text=self.get_school_year(), font=detail_font)
        school_year_label.grid(row=current_row, column=1, padx=20, pady=10)
 
        # Move to the next row
        current_row += 1
 
        # Handle schedule being None
        if schedule is None:
            no_schedule_label = tk.Label(self.stdPOV_root, text="Schedule and section not available yet.", font=detail_font)
            no_schedule_label.grid(row=current_row, column=0, columnspan=3, padx=20, pady=10)
        else:
            # Subject headers
            self.subject_header = tk.Label(self.stdPOV_root, text="Subject", font=title_font)
            self.subject_header.grid(row=current_row, column=0, padx=20, pady=10)
            self.time_header = tk.Label(self.stdPOV_root, text="Time", font=title_font)
            self.time_header.grid(row=current_row, column=1, padx=20, pady=10)
            self.section_header = tk.Label(self.stdPOV_root, text="Teacher", font=title_font)
            self.section_header.grid(row=current_row, column=2, padx=20, pady=10)
 
            # Scrollable area and content
            scrollable_frame = tk.Frame(self.stdPOV_root, height=150)
            scrollable_frame.grid(row=current_row + 1, column=0, columnspan=3, padx=20, pady=5, sticky='nsew')
 
            canvas = tk.Canvas(scrollable_frame, height=150, width=650)  # Limit the height of the canvas
            scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
            scrollable_content = tk.Frame(canvas)
 
            scrollable_content.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
 
            canvas.create_window((0, 0), window=scrollable_content, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
 
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
 
            # Dynamically generate labels for each subject, time, and teacher
            for i, (subject, details) in enumerate(schedule.items()):
                subject_label = tk.Label(scrollable_content, text=subject, font=detail_font)
                subject_label.grid(row=i, column=0, padx=20, pady=5)
 
                time_label = tk.Label(scrollable_content, text=details['time'], font=detail_font)
                time_label.grid(row=i, column=1, padx=20, pady=5)
 
                teacher_label = tk.Label(scrollable_content, text=details['teacher'], font=detail_font)
                teacher_label.grid(row=i, column=2, padx=20, pady=5)
 
        # Date issued label and back button - outside the scrollable area
        self.date_label = tk.Label(self.stdPOV_root, text="Date Issued: " + date_issued, font=title_font)
        self.date_label.grid(row=current_row + 2, column=0, padx=20, pady=10, columnspan=3)
 
        # Place the "Back" button at the top-right corner using place()
        self.back_button_pov = tk.Button(self.stdPOV_root, text="Back", font=('Arial', 13), command=self.back_to_main_from_pov)
        self.back_button_pov.place(relx=0.95, rely=0.95, anchor="se")
 
    def get_school_year(self):
        """Returns the current school year."""
        current_year = datetime.now().year
        next_year = current_year + 1
        return f"{current_year}-{next_year}"
 
    def get_current_date(self):
        """Returns the current date."""
        return datetime.now().strftime("%d-%m-%Y")
 
    def show_teacherWindow(self):
        """Displays the teacher registration window."""
        self.root.withdraw()
        self.teacher_root = tk.Toplevel(self.root)
        self.teacher_root.geometry("500x400")
        self.teacher_root.resizable(0, 0)
        self.teacher_root.title("Teacher Registration")
       
        # First Name
        self.teacher_labelFN = tk.Label(self.teacher_root,
                                        text="First Name:",
                                        font=('Arial', 12))
        self.teacher_labelFN.grid(row=0, column=0, padx=10, pady=10)
        self.teacher_entryFN = tk.Entry(self.teacher_root)
        self.teacher_entryFN.grid(row=0, column=1, padx=10, pady=10)
 
        # Middle Name
        self.teacher_labelMN = tk.Label(self.teacher_root,
                                        text="Middle Name:",
                                        font=('Arial', 12))
        self.teacher_labelMN.grid(row=1, column=0, padx=10, pady=10)
        self.teacher_entryMN = tk.Entry(self.teacher_root)
        self.teacher_entryMN.grid(row=1, column=1, padx=10, pady=10)
 
        # Last Name
        self.teacher_labelLN = tk.Label(self.teacher_root,
                                        text="Last Name:",
                                        font=('Arial', 12))
        self.teacher_labelLN.grid(row=2, column=0, padx=10, pady=10)
        self.teacher_entryLN = tk.Entry(self.teacher_root)
        self.teacher_entryLN.grid(row=2, column=1, padx=10, pady=10)
        # --- Grade Level Dropdown ---
        self.teacher_grade_options = [
            "Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4",
            "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10",
            "Grade 11", "Grade 12" ]
       
        self.clicked_teacher_grade = tk.StringVar(self.teacher_root)
        self.clicked_teacher_grade.set(self.teacher_grade_options[0])
 
        # Call the update function here on grade selection
        self.teacher_grade_menu = tk.OptionMenu(
            self.teacher_root, self.clicked_teacher_grade, *self.teacher_grade_options,
            command=self.update_teacher_subject_dropdown)
        self.teacher_grade_menu.grid(row=3, column=0, padx=10, pady=10)
 
        # --- Subject Dropdown (initially hidden) ---
        self.clicked_teacher_subject = tk.StringVar(self.teacher_root)
        self.teacher_subject_menu = tk.OptionMenu(self.teacher_root,
                                                  self.clicked_teacher_subject,
                                                  "")
        # Initially hide the subject dropdown
        self.teacher_subject_menu.grid_forget()
 
        # --- Strand Dropdown (initially hidden) ---
        self.clicked_teacher_strand = tk.StringVar(self.teacher_root)
        self.teacher_strand_menu = tk.OptionMenu(self.teacher_root,
                                                  self.clicked_teacher_strand,
                                                  "")
        # Initially hide the strand dropdown
        self.teacher_strand_menu.grid_forget()
 
        # Submit Button
        self.teacher_button = tk.Button(
            self.teacher_root,
            text="Submit",
            font=('Arial', 13),
            command=lambda: self.store_teacherData(self.teacher_root))
        self.teacher_button.grid(row=5, column=1, padx=10, pady=10)
 
        # Back Button
        self.back_button = tk.Button(self.teacher_root,
                                       text="Back",
                                       font=('Arial', 13),
                                       command=self.back_to_main)
        self.back_button.grid(row=6, column=1, padx=10, pady=10)
        self.teacher_root.protocol("WM_DELETE_WINDOW",
                                   self.on_closing_teacher)
 
    def update_teacher_subject_dropdown(self, *args):
        """Updates the subject and strand dropdowns based on the selected grade level."""
 
        self.selected_grade = self.clicked_teacher_grade.get()
 
        # Manually defined subject options for K-12
        self.subject_options = {
            "Kindergarten": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 1": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 2": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 3": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 4": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 5": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 6": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 7": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 8": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 9": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 10": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 11": {
                "ABM": ["Accountancy, Business, and Management (ABM)", "Organization and Management", "Applied Economics", "Business Math", "Business Ethics and Social Responsibility"],
                "STEM": ["Science, Technology, Engineering, and Mathematics (STEM)", "General Biology", "General Chemistry", "Pre-Calculus", "Basic Calculus"],
                "HUMSS": ["Humanities and Social Sciences (HUMSS)", "Creative Writing", "Creative Nonfiction", "World Religions", "Philippine Politics and Governance"],
                "GAS": ["General Academic Strand (GAS)", "Oral Communication", "Reading and Writing", "Komunikasyon at Pananaliksik", "Pagbasa at Pagsusuri"],
                "ICT": ["Information Communication, and Technology(ICT)", "Understanding Culture Society and Politics", "Media Information", "Oral Communication", "Computer System Servicing", "Food(Fish) Processing", "Reading and Writing", "Komunikasyon at Pananaliksik", "Pagbasa at Pagsusuri"]
                # ... (add other strands and their subjects)
            },
            "Grade 12": {
                "ABM": ["Business Finance", "Principles of Marketing", "Business Enterprise Simulation"],
                "STEM": ["General Physics", "General Biology 2", "General Chemistry 2"],
                "HUMSS": ["Introduction to World Religions and Belief Systems", "Creative Nonfiction", "Trends, Networks, and Critical Thinking"],
                "GAS": ["Media and Information Literacy", "Contemporary Philippine Arts from the Regions"],
                "ICT": ["Information Communication, and Technology(ICT)", "Understanding Culture Society and Politics", "Media Information", "Oral Communication", "Computer System Servicing", "Food(Fish) Processing", "Reading and Writing", "Komunikasyon at Pananaliksik", "Pagbasa at Pagsusuri"]
                # ... (add other strands and their subjects)
            }
        }
 
        if self.selected_grade in ["Grade 11", "Grade 12"]:
            # Show strand dropdown and hide subject dropdown
            self.teacher_subject_menu.grid_forget()
            self.teacher_strand_menu.grid(row=3, column=1, padx=10, pady=10)
 
            # Populate strand dropdown
            available_strands = list(self.subject_options[self.selected_grade].keys())
            self.teacher_strand_menu['menu'].delete(0, 'end')
            for strand in available_strands:
                self.teacher_strand_menu['menu'].add_command(
                    label=strand,
                    command=tk._setit(self.clicked_teacher_strand, strand))
            if available_strands:
                self.clicked_teacher_strand.set(available_strands[0])
 
            # Bind strand selection change to a callback
 
            self.clicked_teacher_strand.trace_add("write", lambda *args: self.update_subject_dropdown_from_strand())
 
            # Update subject dropdown based on selected strand
            self.update_subject_dropdown_from_strand()
        else:
            # Show subject dropdown and hide strand dropdown
            self.teacher_strand_menu.grid_forget()
            self.teacher_subject_menu.grid(row=3, column=1, padx=10, pady=10)
 
            # Populate subject dropdown
            available_subjects = self.subject_options[self.selected_grade]
            self.teacher_subject_menu['menu'].delete(0, 'end')
            for subject in available_subjects:
                self.teacher_subject_menu['menu'].add_command(
                    label=subject,
                    command=tk._setit(self.clicked_teacher_subject, subject))
            if available_subjects:
                self.clicked_teacher_subject.set(available_subjects[0])
       
    def update_subject_dropdown_from_strand(self):
        """Updates the subject dropdown based on the selected strand."""
        selected_strand = self.clicked_teacher_strand.get()
        available_subjects = self.subject_options[self.selected_grade][selected_strand]
 
        self.teacher_subject_menu['menu'].delete(0, 'end')
        for subject in available_subjects:
            self.teacher_subject_menu['menu'].add_command(
                label=subject,
                command=tk._setit(self.clicked_teacher_subject, subject))
        if available_subjects:
            self.clicked_teacher_subject.set(available_subjects[0])
        self.teacher_subject_menu.grid(row=3, column=2, padx=10, pady=10)  # Show the subject dropdown
 
    def store_teacherData(self, teacher_root):  # Add teacher_root as argument
        """Stores teacher data and validates input."""
        first_name = self.teacher_entryFN.get().strip().title()
        middle_name = self.teacher_entryMN.get().strip().title()
        last_name = self.teacher_entryLN.get().strip().title()
        subject = self.clicked_teacher_subject.get()
        grade_level = self.clicked_teacher_grade.get()  # Get the grade level
 
        # Validate input
        if not all([first_name, last_name, subject]):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
 
        if not first_name.replace(" ", "").isalpha() or not last_name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Names should only contain letters and spaces.")
            return
 
        # Initialize teacher data with an empty schedule dictionary
        teacher_data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'subject': subject,
            'grade_level': grade_level,
            'date_issued': self.get_current_date(),
            'schedule': None  # Initialize with None or empty dictionary
        }
 
        # Check if teacher already exists
        if not any(t['first_name'] == first_name
                and t['middle_name'] == middle_name
                and t['last_name'] == last_name for t in self.teachers):
            # Add new teacher if not already in self.teachers
            self.teachers.append(teacher_data)
            self.save_data()
            messagebox.showinfo("Success", "Teacher added successfully!")
            teacher_root.destroy()  # Close teacher_root after successful submission
 
            # Initially pass schedule=None when adding a new teacher
            self.show_teacherPOV(first_name, middle_name, last_name, subject, teacher_data['date_issued'], teacher_data['schedule'])
        else:
            # Retrieve the existing teacher from self.teachers
            existing_teacher = next(t for t in self.teachers
                                    if t['first_name'] == first_name
                                    and t['middle_name'] == middle_name
                                    and t['last_name'] == last_name)
 
            # Pass the existing teacher data and schedule to show_teacherPOV
            self.show_teacherPOV(existing_teacher['first_name'],
                                existing_teacher['middle_name'],
                                existing_teacher['last_name'],
                                existing_teacher['subject'],
                                existing_teacher['date_issued'],
                                existing_teacher['schedule'])
 
    def show_teacherPOV(self, first_name, middle_name, last_name, subject, date_issued, schedule):
        """Displays the teacher point of view window."""
        self.tchPOV_root = tk.Toplevel(self.root)  # Use Toplevel
        self.tchPOV_root.geometry("800x450")
        self.tchPOV_root.resizable(0, 0)
        self.tchPOV_root.title("Schedule System Organizer: Teacher")
 
        display_text = f"{first_name} {middle_name} {last_name}\nSubject: {subject}"
        title_font = ('Arial', 12, 'bold')
        detail_font = ('Arial', 12)
 
        # Center the header text
        self.tchOutput = tk.Label(self.tchPOV_root, text=display_text, font=('Arial', 20), anchor='center')
        self.tchOutput.grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky='ew')
 
        # Header labels for time, grade, strand, and section
        self.time_header = tk.Label(self.tchPOV_root, text="Time", font=title_font, anchor='center')
        self.time_header.grid(row=2, column=0, padx=20, pady=10, sticky='ew')
 
        self.grade_header = tk.Label(self.tchPOV_root, text="Grade", font=title_font, anchor='center')
        self.grade_header.grid(row=2, column=1, padx=20, pady=10, sticky='ew')
 
        self.strand_header = tk.Label(self.tchPOV_root, text="Strand", font=title_font, anchor='center')
        self.strand_header.grid(row=2, column=2, padx=20, pady=10, sticky='ew')
 
        self.section_header = tk.Label(self.tchPOV_root, text="Section", font=title_font, anchor='center')
        self.section_header.grid(row=2, column=3, padx=20, pady=10, sticky='ew')
 
        # Scrollable area and content
        scrollable_frame = tk.Frame(self.tchPOV_root, height=150)
        scrollable_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=5, sticky='nsew')
 
        canvas = tk.Canvas(scrollable_frame, height=150, width=650)  # Limit the height of the canvas
        scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
        scrollable_content = tk.Frame(canvas)
 
        scrollable_content.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
 
        canvas.create_window((0, 0), window=scrollable_content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
 
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
 
        # Display the schedule if it exists
        if schedule:
            for i, entry in enumerate(schedule):
                # Dynamically generate labels for time, grade, strand, and section
                time_label = tk.Label(scrollable_content, text=entry['time'], font=detail_font, anchor='center')
                time_label.grid(row=i, column=0, padx=20, pady=5, sticky='ew')
 
                grade_label = tk.Label(scrollable_content, text=entry['grade'], font=detail_font, anchor='center')
                grade_label.grid(row=i, column=1, padx=20, pady=5, sticky='ew')
 
                strand_label = tk.Label(scrollable_content, text=entry['strand'], font=detail_font, anchor='center')
                strand_label.grid(row=i, column=2, padx=20, pady=5, sticky='ew')
 
                section_label = tk.Label(scrollable_content, text=entry['section'], font=detail_font, anchor='center')
                section_label.grid(row=i, column=3, padx=20, pady=5, sticky='ew')
        else:
            # Handle case when no schedule exists for the teacher
            no_schedule_label = tk.Label(self.tchPOV_root, text="No schedule available for this teacher.", font=detail_font, anchor='center')
            no_schedule_label.grid(row=3, column=0, columnspan=4, padx=20, pady=10, sticky='ew')
 
        # Date issued label and back button - outside the scrollable area
        self.date_label = tk.Label(self.tchPOV_root, text="Date Issued: " + date_issued, font=title_font, anchor='center')
        self.date_label.grid(row=4, column=0, padx=20, pady=10, columnspan=3, sticky='ew')
 
        self.back_button_pov = tk.Button(self.tchPOV_root, text="Back", font=('Arial', 13), command=self.back_to_main_from_pov)
        self.back_button_pov.place(relx=0.95, rely=0.95, anchor="se")
 
   
    def generate_schedule(self):
        """Generates and displays the schedule in a table format and updates student schedule data."""
       
        schedule_window = tk.Toplevel(self.admin_root)
        schedule_window.geometry("1000x600")  # Adjust size as needed
        schedule_window.title("Generated Schedule")
 
        # Create Treeview widget
        schedule_table = ttk.Treeview(schedule_window,
                                    columns=("Student", "Section", "Grade", "Strand", "Subject", "Time", "Teacher"),
                                    show="headings")
        schedule_table.heading("Student", text="Student")
        schedule_table.heading("Section", text="Section")
        schedule_table.heading("Grade", text="Grade")
        schedule_table.heading("Strand", text="Strand")
        schedule_table.heading("Subject", text="Subject")
        schedule_table.heading("Time", text="Time")
        schedule_table.heading("Teacher", text="Teacher")
 
        sections = {}
        section_count = {}
        max_class_size = 30
 
        # Initialize teacher schedules as empty lists
        for teacher in self.teachers:
            teacher['schedule'] = []
 
        subject_to_teacher = {}
        for teacher in self.teachers:
            subject = teacher.get('subject')
            if subject:
                teacher_name = f"{teacher['first_name']} {teacher['middle_name']} {teacher['last_name']}"
                subject_to_teacher[subject] = teacher_name
 
        start_time = datetime.strptime("06:00 AM", "%I:%M %p")
        end_time = datetime.strptime("5:00 PM", "%I:%M %p")
 
        # Loop through each student and generate or overwrite the schedule for them
        for student in self.students:
            name = f"{student['first_name']} {student['middle_name']} {student['last_name']}"
            grade = student['grade']
            strand = student['strand'] if 'strand' in student else ""
            sectioning = (grade, strand)  # Create a grade level based on grade and strand
 
            if sectioning not in sections:
                sections[sectioning] = []
                section_count[sectioning] = 1  # Initialize section count
 
            if len(sections[sectioning]) < max_class_size:
                student['section'] = f"{section_count[sectioning]:02d}"
                sections[sectioning].append(student)
            else:
                section_count[sectioning] += 1
                sections[sectioning] = [student]
                student['section'] = f"{section_count[sectioning]:02d}"
 
            section = student.get('section', 'N/A')
           
            # Get subjects for the student's grade
            subjects = self.get_subjects_for_grade(grade)
            if isinstance(subjects, dict):
                strand = student.get('strand', 'N/A')
                subjects = subjects.get(strand, [])
 
            unique_subjects = set(subjects)
            current_time = start_time
            class_count = 0
 
            # Initialize a new schedule for the student
            student_schedule = {}
 
            for subject in unique_subjects:
                start_subject_time = current_time.strftime("%I:%M %p")
                end_subject_time = (current_time + timedelta(minutes=40)).strftime("%I:%M %p")
                teacher_name = subject_to_teacher.get(subject, 'N/A')
 
                # Add subject to student's schedule
                student_schedule[subject] = {
                    'time': f"{start_subject_time} to {end_subject_time}",
                    'teacher': teacher_name
                }
 
                # Insert data into the Treeview table
                schedule_table.insert("", tk.END, values=(name, section, grade, strand, subject, f"{start_subject_time} to {end_subject_time}", teacher_name))
               
                # Update the teacher's schedule
                if teacher_name != 'N/A':
                    for teacher in self.teachers:
                        if f"{teacher['first_name']} {teacher['middle_name']} {teacher['last_name']}" == teacher_name:
                            # Check if the teacher is already teaching at the same time
                            time_conflict = any(
                                entry['time'] == f"{start_subject_time} to {end_subject_time}"
                                for entry in teacher['schedule']
                            )
 
                            # Skip assigning this teacher if they are already teaching at the same time
                            if time_conflict:
                                continue  # Skip to the next subject and don't assign this teacher
 
                            # Check if the same grade, strand, section, and time already exist in the teacher's schedule
                            duplicate_entry = any(
                                entry['time'] == f"{start_subject_time} to {end_subject_time}" and
                                entry['grade'] == grade and
                                entry['strand'] == (strand if strand else 'N/A') and
                                entry['section'] == section
                                for entry in teacher['schedule']
                            )
                           
                            # Only append to the teacher's schedule if the entry is not a duplicate
                            if not duplicate_entry:
                                teacher['schedule'].append({
                                    'subject': subject,
                                    'time': f"{start_subject_time} to {end_subject_time}",
                                    'grade': grade,
                                    'strand': strand if strand else 'N/A',  # Add strand or 'N/A' if none
                                    'section': section
                                })
 
                current_time += timedelta(minutes=40)
                class_count += 1
 
                if class_count == 4:
                    if grade in ["Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6"]:
                        current_time += timedelta(minutes=30)  # 30-minute break for K-6
                    elif grade in ["Grade 7", "Grade 8", "Grade 9", "Grade 10"]:
                        current_time += timedelta(minutes=30)  # 30-minute break for Grade 7-10
                    elif grade in ["Grade 11", "Grade 12"]:
                        current_time += timedelta(minutes=20)  # 20-minute break for Grade 11-12
 
                if current_time >= end_time:
                    break
 
            # Update student's schedule
            student['schedule'] = student_schedule
 
        # Define a function to save, close the window, and refresh the admin window
        def close_schedule_and_refresh():
            self.save_data()  # Save the data
            schedule_window.destroy()  # Close the schedule window
            self.admin_root.destroy()  # Close the existing admin window
            self.show_adminWindow()  # Reopen the admin window to refresh with updated data
 
        # Display the schedule table
        schedule_table.pack(expand=True, fill='both')
        # Back button to bind the close and refresh action
        back_button_schedule = tk.Button(schedule_window, text="Close", command=close_schedule_and_refresh)
        back_button_schedule.pack(pady=10)
 
 
   
    def show_adminpassWindow(self):
        """Displays the admin password entry window."""
        self.adminpass_window = tk.Toplevel(self.root)
        self.adminpass_window.geometry("400x200")
        self.adminpass_window.title("Admin Password")
        self.password_label = tk.Label(self.adminpass_window,
                                       text="Enter Admin Password:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.adminpass_window, show="*")
        self.password_entry.pack(pady=10)
        self.password_button = tk.Button(self.adminpass_window,
                                          text="Submit",
                                          command=self.validate_password)
        self.password_button.pack(pady=10)
 
    def validate_password(self):
        """Validates the admin password."""
        entered_password = self.password_entry.get()
        if entered_password == "admin123":
            messagebox.showinfo("Access Granted", "Welcome Admin!")
            self.adminpass_window.destroy()
            self.show_adminWindow()
        else:
            messagebox.showerror("Access Denied", "Incorrect Password!")
            self.password_entry.delete(0, tk.END)
 
    def show_adminWindow(self):
        """Displays the admin panel window."""
        self.root.withdraw()
        self.admin_root = tk.Tk()
        self.admin_root.geometry("1000x700")
        self.admin_root.title("Schedule System Organizer: Admin")
        self.admin_label = tk.Label(self.admin_root,
                                    text="Admin Panel",
                                    font=('Arial', 24))
        self.admin_label.pack(pady=20)
   
        # --- Students Table ---
        self.student_table = ttk.Treeview(self.admin_root,
                                        columns=("Name", "Grade Level", "Strand", "Section"),
                                        show="headings")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Grade Level", text="Grade Level")
        self.student_table.heading("Strand", text="Strand")
        self.student_table.heading("Section", text="Section")
 
        for student in self.students:
            name = f"{student['first_name']} {student['middle_name']} {student['last_name']}"
            grade = student['grade']
            strand = student['strand'] if 'strand' in student else ""
            section = student['section']  
            self.student_table.insert("", tk.END, values=(name, grade, strand, section))
 
        self.student_table.pack(pady=10, fill='both', expand=True)
   
        # --- Teachers Table ---
        self.teacher_table = ttk.Treeview(self.admin_root,
                                        columns=("Name", "Subject", "Time", "Grade", "Strand", "Section"),
                                        show="headings")
        self.teacher_table.heading("Name", text="Name")
        self.teacher_table.heading("Subject", text="Subject")
        self.teacher_table.heading("Time", text="Time")
        self.teacher_table.heading("Grade", text="Grade")
        self.teacher_table.heading("Strand", text="Strand")
        self.teacher_table.heading("Section", text="Section")
 
        for teacher in self.teachers:
            name = f"{teacher['first_name']} {teacher['middle_name']} {teacher['last_name']}"
            if 'schedule' in teacher and teacher['schedule']:
                # Loop through each schedule entry for the teacher
                for entry in teacher['schedule']:
                    subject = entry['subject']
                    time = entry['time']
                    grade = entry['grade']
                    strand = entry['strand']
                    section = entry['section']
                    self.teacher_table.insert("", tk.END, values=(name, subject, time, grade, strand, section))
            else:
                # If no schedule exists, just display the teacher's name and subject
                self.teacher_table.insert("", tk.END, values=(name, teacher['subject'], "N/A", "N/A", "N/A", "N/A"))
 
        self.teacher_table.pack(pady=10, fill='both', expand=True)
 
        # Generate schedule button
        self.schedule_button = tk.Button(self.admin_root,
                                        text="Generate Schedule",
                                        command=self.generate_schedule)
        self.schedule_button.pack()
 
        # Back button
        self.back_button_admin = tk.Button(self.admin_root,
                                        text="Back",
                                        font=('Arial', 13),
                                        command=self.back_to_main_from_admin)
        self.back_button_admin.pack()
 
    def get_subjects_for_grade(self, grade):
        """Returns the list of subjects for a given grade level."""
 
        # Manually defined subject options for K-12
        subject_options = {
            "Kindergarten": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 1": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 2": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 3": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 4": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 5": ["Reading", "Writing", "Math", "Science", "Social Studies", "Art", "Music", "Physical Education"],
            "Grade 6": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 7": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 8": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 9": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 10": ["English", "Filipino", "Math", "Science", "Araling Panlipunan", "MAPEH", "TLE"],
            "Grade 11": {
                "ABM": ["Accountancy, Business, and Management (ABM)", "Organization and Management", "Applied Economics", "Business Math", "Business Ethics and Social Responsibility"],
                "STEM": ["Science, Technology, Engineering, and Mathematics (STEM)", "General Biology", "General Chemistry", "Pre-Calculus", "Basic Calculus"],
                "HUMSS": ["Humanities and Social Sciences (HUMSS)", "Creative Writing", "Creative Nonfiction", "World Religions", "Philippine Politics and Governance"],
                "GAS": ["General Academic Strand (GAS)", "Oral Communication", "Reading and Writing", "Komunikasyon at Pananaliksik", "Pagbasa at Pagsusuri"],
                # ... (add other strands and their subjects)
            },
            "Grade 12": {
                "ABM": ["Business Finance", "Principles of Marketing", "Business Enterprise Simulation"],
                "STEM": ["General Physics", "General Biology 2", "General Chemistry 2"],
                "HUMSS": ["Introduction to World Religions and Belief Systems", "Creative Nonfiction", "Trends, Networks, and Critical Thinking"],
                "GAS": ["Media and Information Literacy", "Contemporary Philippine Arts from the Regions"],
                # ... (add other strands and their subjects)
            }
        }
 
        return subject_options.get(grade, [])
 
    def back_to_main(self):
        """Returns to the main window."""
        if hasattr(self, 'student_root') and self.student_root.winfo_exists():
            self.student_root.withdraw()
        if hasattr(self, 'teacher_root') and self.teacher_root.winfo_exists():
            self.teacher_root.withdraw()
        self.root.deiconify()
 
    def back_to_main_from_pov(self):
        """Returns to the main window from the student/teacher POV."""
        try:
            if self.stdPOV_root.winfo_exists():
                self.stdPOV_root.withdraw()
        except AttributeError:
            pass
        try:
            if self.tchPOV_root.winfo_exists():
                self.tchPOV_root.withdraw()
        except AttributeError:
            pass
        self.root.deiconify()
 
    def back_to_main_from_admin(self):
        """Returns to the main window from the admin panel."""
        if hasattr(self, 'admin_root') and self.admin_root.winfo_exists():
            self.admin_root.withdraw()
        self.root.deiconify()
 
    def on_closing(self):
        """Handles the main window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
 
    def on_closing_student(self):
        """Handles the student window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.student_root.destroy()
            self.root.deiconify()
 
    def on_closing_teacher(self):
        """Handles the teacher window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.teacher_root.destroy()
            self.root.deiconify()
 
    def save_data(self):
        """Saves student and teacher data."""
        with open("students_data.pkl", "wb") as f:
            pickle.dump(self.students, f)
        with open("teachers_data.pkl", "wb") as f:
            pickle.dump(self.teachers, f)
 
    def load_data(self):
        """Loads student and teacher data."""
        if os.path.exists("students_data.pkl"):
            with open("students_data.pkl", "rb") as f:
                self.students = pickle.load(f)
        else:
            self.students = []
        if os.path.exists("teachers_data.pkl"):
            with open("teachers_data.pkl", "rb") as f:
                self.teachers = pickle.load(f)
        else:
            self.teachers = []
 
firstWindow()