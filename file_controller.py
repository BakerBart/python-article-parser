def read_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def save_html_to_file(content, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)