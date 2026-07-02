"""
                         STUDENT DATA ORGANIZER DOCUMENTATION
================================================================================

PROJECT OVERVIEW:

The Student Data Organizer is a menu driven program that allows users to 
manage student records efficiently.The program provides functionalities 
to add, display, update, and delete student records, as well as list
unique subjects.This documentation provides an overview of the program's 
features, usage instructions, and implementation details. we have used a dictionary
to store the student records, where each student ID serves as a unique key, 
and the corresponding value is a dictionary containing the student's details such as 
name, age, grade, subject, and date of birth.We have used lists to maintain the order 
of student records and sets to store unique subjects.The program is designed to be 
user-friendly, with clear prompts and error handling to ensure a smooth user experience. 
The program is implemented in Python and can be run in any Python environment.

"""

import sys

student_data_dict = {}
student_records_list = []
unique_subjects_set = set()

print("\n=== Welcome to the Student Data Organizer ===")
print(sys.modules[__name__].__doc__) 
print("================================================================================")

while True:

    print(" ")
    print("\n--- Main Menu ---")
    print(" ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. List Subjects")
    print("6. Exit")
    choice = input("\nEnter your choice: ")

    match choice:
        case '1':
            def choice1_doc():
                """[DOCUMENTATION]: User has to enter the student details such as ID, name, age, etc., 
                   to add a new student profile to the database. The function checks for duplicate IDs 
                   and ensures that the age is an integer.We have also added a condition to check if 
                   the student ID already exists in the database before attempting to add a new student 
                   profile and provide the user with an error message if the ID is already in use.We have 
                   also ensured that the student ID is added to both the dictionary and the list of 
                   student records to maintain data integrity.To do so we have used a tuple to 
                   store the immutable information (student ID and date of birth) and a set to store t
                   he unique subjects.we have type caseted the age to an integer to ensure that it is 
                   stored as a number in the database.Ones the task is completed it will display a message
                   indicating that the student was added successfully."""

            print(choice1_doc.__doc__)
            print("==========================================================================================")
            print("\n--- Enter Student Details ---\n")
            student_id = input("Student ID: ")

            if student_id in student_data_dict:
                print("Error: This ID already exists.")
            else:
                name = input("Name: ")
                age = int(input("Age: ")) 
                grade = input("Grade: ")
                dob = input("Date of Birth: ")
                subject = input("Enter one major subject: ")

                immutable_info = (student_id, dob)
                unique_subjects_set.add(subject)

                student_profile = {
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "subject": subject,
                    "dob": dob,
                    "identity": immutable_info
                }

                student_data_dict[student_id] = student_profile
                student_records_list.append(student_id)
                print("Student added successfully!")

        case '2':
            def choice2_doc():
                """[DOCMENTATION]: User can view all the student records in the database.
                We have conditioned it to check if there are any records available.
                If not, it will display a message indicating that no records were found 
                else it will display the student records in a formatted manner."""

            print(choice2_doc.__doc__)
            print("================================================================================")
            print("\n--- Displaying All Students ---")
            if len(student_records_list) == 0:
                print("No records found.")
            else:
                for s_id in student_records_list:
                    profile = student_data_dict[s_id]
                    print("ID:", s_id, "| Name:", profile["name"], "| Age:", profile["age"], "| Date of Birth:", profile["dob"], "| Grade:", profile["grade"], "| Subject:", profile["subject"])

        case '3':
            def choice3_doc():
                """[DOCMENTATION]:User can update the student information in the database.
                we have conditioned it to check if the student ID exists in the database.We have
                also added a condition to check if the student ID exists in the database before 
                attempting to update it and provide the user with an error message if the ID 
                is not found.Ones the task is completed it will display a message indicating 
                that the information was updated successfully.Ones the task is completed it will
                display a message indicating that the information was updated successfully."""

            print(choice3_doc.__doc__)
            print("================================================================================")
            print("\n--- Update Student ---")
            student_id = input("Enter Student ID to update: ")

            if student_id not in student_data_dict:
                print("Error: Student not found.")
            else:
                new_name = input("Enter New Name: ")
                new_age = input("Enter New Age: ")
                new_grade = input("Enter New Grade: ")
                new_subject = input("Enter New Subject: ")

                student_data_dict[student_id]["name"] = new_name
                student_data_dict[student_id]["age"] = int(new_age)
                student_data_dict[student_id]["grade"] = new_grade
                student_data_dict[student_id]["subject"] = new_subject
                print("\n\n Information updated successfully!")

        case '4':

            def choice4_doc():
                """[DOCMENTATION]: User can delete a student record from the database by providing
                    the student ID.We have also added a condition to check if the student ID exists 
                    in the database before attempting to delete it and provide the user with an
                    error message if the ID is not found.We have also ensured that the student ID is 
                    removed from both the dictionary and the list of student records to maintain 
                    data integrity.To so we have used the del statement to remove the student record 
                    from the dictionary and the remove() method to remove the student ID from the 
                    list of student records.Ones the task is completed it will display a message 
                    indicating that the student record was deleted successfully."""
            print(choice4_doc.__doc__)
            print("===================================================================================")
            print("\n--- Delete Student ---")
            student_id = input("Enter Student ID to delete: ")

            if student_id in student_data_dict:
                del student_data_dict[student_id]
                student_records_list.remove(student_id)
                print("Student record deleted.")
            else:
                print("Error: Student ID not found.")

        case '5':
            def choice5_doc():
                """[DOCMENTATION]: User can view a list of all unique subjects provided to
                the students in the database.We have also added a condition to check if there 
                are any subjects available in the database before attempting to display them 
                and provide the user with an error message if no subjects are found:to do so we
                have used a set to store the unique subjects and then displayed them in a 
                formatted manner then used len() to add the required condition."""
            print(choice5_doc.__doc__)
            print("================================================================================")
            print("\n--- List of Subjects ---")
            if len(unique_subjects_set) == 0:
                print("No subjects found.")
            else:
                for item in unique_subjects_set:
                    print("-", item)

        case '6':
            def choice6_doc():
                """[DOCMENTATION]:Here the user can exit the program and it will display a goodbye message."""
            print(choice6_doc.__doc__)
            print("================================================================================")
            print("\nGoodbye!-Thank you for using the Student Data Organizer.")
            break

        case _:
            print("Invalid choice. Try again.")
