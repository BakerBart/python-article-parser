def generate_preview(template_path, article_path, output_path):
  try:
    with open(template_path, "r", encoding="utf-8") as template_file:
      template_content = template_file.read()

    with open(article_path, "r", encoding="utf-8") as article_file:
      article_content = article_file.read()

    full_content = template_content.replace("<!-- Paste your article content here -->", article_content)

    with open(output_path, "w", encoding="utf-8") as output_file:
      output_file.write(full_content)

  except Exception as e:
    raise IOError(f"Error while generating preview: {e}")