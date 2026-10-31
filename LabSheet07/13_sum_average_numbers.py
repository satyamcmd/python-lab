# 13. Read numbers (one per line or separated by spaces) and show sum and average.
try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        numbers = [float(value) for value in file.read().split()]
    if numbers:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("The file contains no numbers.")
except FileNotFoundError:
    print("Create numbers.txt first, with numbers separated by spaces or lines.")
except ValueError:
    print("The file contains a value that is not a number.")
