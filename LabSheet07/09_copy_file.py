# 9. Copy all content from one text file into another.
source_name = "sample.txt"
destination_name = "copy.txt"
try:
    with open(source_name, "r", encoding="utf-8") as source:
        content = source.read()
    with open(destination_name, "w", encoding="utf-8") as destination:
        destination.write(content)
    print("Copied", source_name, "to", destination_name)
except FileNotFoundError:
    print("Source file was not found.")
except OSError as error:
    print("File error:", error)
