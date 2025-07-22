import re
import os

def replace_strong_tags_in_file(input_path):
    # Split the input path into directory, base name, and extension
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_numbered{ext}"

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    def replacer(match):
        nonlocal count
        count += 1
        return f"<strong>{count}. "

    new_content = re.sub(r"<strong>", replacer, content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Processed file saved as: {output_path}")

if __name__ == "__main__":
    input_file = "README.md"  # Replace with the actual file path
    replace_strong_tags_in_file(input_file)