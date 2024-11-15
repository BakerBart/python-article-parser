def read_article(file_path):
  try:
    with open(file_path, "r", encoding="utf-8") as file:
      return file.read()
  except FileNotFoundError:
    raise FileNotFoundError(f"File '{file_path}' not found.")
  except Exception as e:
    raise IOError(f"Error reading file '{file_path}': {e}")

def save_html_to_file(content, output_file):
  try:
    with open(output_file, "w", encoding="utf-8") as file:
      file.write(content)
  except Exception as e:
    raise IOError(f"Error saving file '{output_file}': {e}")