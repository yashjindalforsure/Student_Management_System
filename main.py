from student import (
    add_student,
    view_students,
    search_student,
    calculate_average,
    get_integer
)

from file_handler import load_students, save_students

def greet():
    print("====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")

students = load_students()

while True:
    greet()

    choice = get_integer("Enter your choice: ")

    if choice == 1:
       add_student(students)
       save_students(students)

    elif choice == 2:
       view_students(students)

    elif choice == 3:
       search_student(students)

    elif choice == 4:
       calculate_average(students)

    elif choice == 5:
       print("Exiting Program")
       break

    else:
       print("INVALID CHOICE!!!")