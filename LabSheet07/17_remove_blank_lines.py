# 17. Remove blank/whitespace-only lines and save the cleaned content.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    nonblank_lines = [line for line in lines if line.strip()]
    with open("without_blank_lines.txt", "w", encoding="utf-8") as file:
        file.writelines(nonblank_lines)
    print("Cleaned content saved to without_blank_lines.txt.")
except FileNotFoundError:
    print("sample.txt was not found.")
