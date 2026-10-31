# 7. Take multiple lines from the user and write them to a file.
print("Enter lines. Type END on a separate line to finish.")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

try:
    with open("user_lines.txt", "w", encoding="utf-8") as file:
        file.write("\\n".join(lines))
        if lines:
            file.write("\\n")
    print("Lines saved to user_lines.txt.")
except OSError as error:
    print("File error:", error)
