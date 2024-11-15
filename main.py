from file_controller import read_article, save_html_to_file
from api_controller import generate_html_with_openai

def main():
    article_file = "source_text.txt"
    output_html_file = "artykul.html"

    try:
        article_content = read_article(article_file)

        generated_html = generate_html_with_openai(article_content)

        save_html_to_file(generated_html, output_html_file)

        print(f"HTML article saved to {output_html_file}.")

    except (FileNotFoundError, IOError) as e:
        print(f"File error: {e}")
    except RuntimeError as e:
        print(f"API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
    