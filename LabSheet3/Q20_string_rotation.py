# Q20: Check if two strings are rotations of each other
# Idea: B is a rotation of A only if lengths match and B appears inside A + A
first = input("Enter first string: ")
second = input("Enter second string: ")
if len(first) != len(second):
    print("NOT rotations (lengths differ).")
elif second in first + first:
    print(f'"{second}" is a rotation of "{first}".')
else:
    print(f'"{second}" is NOT a rotation of "{first}".')
