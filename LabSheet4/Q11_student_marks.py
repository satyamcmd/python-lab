# Q11: Create a dictionary of student names and marks and display it
n = int(input("Enter number of students: "))
if n < 1:
    print("Enter at least one student.")
else:
    marks_dict = {}
    for i in range(n):
        name = input(f"Enter name of student {i + 1}: ")
        marks = int(input(f"Enter marks of {name} (0-100): "))
        while marks < 0 or marks > 100:   # input validation
            marks = int(input("Invalid! Enter marks between 0 and 100: "))
        marks_dict[name] = marks
    print("\nStudent Marks Dictionary:", marks_dict)
    print(f"\n{'Name':<15}{'Marks':>6}")
    print("-" * 21)
    for name in marks_dict:
        print(f"{name:<15}{marks_dict[name]:>6}")
