def get_integer(message):
   while True:
      try:
         return int(input(message))
      except ValueError:
         print("Please enter a valid number.")

def get_marks():
   while True:
      m = get_integer("Enter marks: ")

      if 0 <= m <= 100:
         return m

      print("Invalid marks! Enter between 0 and 100.")

def add_student(students):

    while True:
       name = input("Enter name: ").strip()

       if name:
          break

       print("Name cannot be empty.")
    while True:
       roll = get_integer("Enter roll number: ")

       if roll > 0:
          break

       print("Roll number must be positive.")

    exists = False

    for student in students:
       if student["Roll No."] == roll:
          exists = True
          break

    if exists:
       print("Roll number already exists.")
       return

    marks = []

    for i in range(3):
       m = get_marks()
       marks.append(m)

    student = {
       "Name": name,
       "Roll No.": roll,
       "Marks": marks
   }

    students.append(student)

    print("Student added successfully.")

def view_students(students):
   
   print("===== STUDENT RECORDS =====")

   if len(students) == 0:
      print("No student records found.")

   else:
      print(f"{'Name':<15}{'Roll No.':<12}{'Marks':<20}{'Average':<12}")
      for student in students:
         marks = ", ".join(map(str, student["Marks"]))
         average = sum(student["Marks"]) / len(student["Marks"])
         print(f"{student['Name']:<15}{student['Roll No.']:<12}{marks:<20}{average:<12.2f}")

      print("-------------------------------------------------------------")

def search_student(students):
   
   roll = get_integer("Enter roll number to search: ")

   found = False

   for student in students:
      if student["Roll No."] == roll:
         found = True

         print("Student Found!")

         for key,values in student.items():
            print(key,":",values)

         break

   if found == False:
      print("Student not found.")

def calculate_average(students):
   
   roll = get_integer("Enter roll number: ")

   found = False

   for student in students:
      if student["Roll No."] == roll:
         found = True
         marks = student["Marks"]

         total = sum(marks)
         average = total / len(marks)

         print("Average:",average)
         break

   if not found:
      print("Student not found.")