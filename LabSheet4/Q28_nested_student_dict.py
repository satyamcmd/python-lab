# Q28: Create a nested dictionary for student details (Name, Roll, Marks)
n = int(input("Enter number of students: "))
if n < 1:
    print("Enter at least one student.")
else:
    students = {}
    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("  Name : ")
        roll = int(input("  Roll : "))
        marks = int(input("  Marks: "))
        # inner dictionary holds one student's details
        students[f"Student{i + 1}"] = {"Name": name, "Roll": roll, "Marks": marks}
    print("\nNested dictionary:")
    print(students)
    print(f"\n{'ID':<10}{'Name':<15}{'Roll':>6}{'Marks':>7}")
    print("-" * 38)
    for student_id in students:
        details = students[student_id]
        print(f"{student_id:<10}{details['Name']:<15}{details['Roll']:>6}{details['Marks']:>7}")
