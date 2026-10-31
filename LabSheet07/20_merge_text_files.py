# 20. Merge two text files into a third file.
try:
    with open("file1.txt", "r", encoding="utf-8") as first:
        content1 = first.read()
    with open("file2.txt", "r", encoding="utf-8") as second:
        content2 = second.read()
    with open("merged.txt", "w", encoding="utf-8") as output:
        output.write(content1)
        if content1 and not content1.endswith("\\n"):
            output.write("\\n")
        output.write(content2)
    print("Merged content saved to merged.txt.")
except FileNotFoundError as error:
    print("Required input file not found:", error.filename)
