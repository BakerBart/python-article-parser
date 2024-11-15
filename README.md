# HTML Article Generator

A Python application that processes a text-based article, generates an HTML representation using OpenAI's API, and creates both a preview-ready template and a complete HTML preview.

## Features

-   Reads an article from a text file.
-   Generates HTML using OpenAI API with gpt-4o model.
-   Saves the generated HTML to a file.
-   Combines the generated HTML with a template to produce a full article preview.

---
## Requirements

-   Python 3.13
-   OpenAI Python library
---

## Installation

1.  Clone the repository:

    
    `git clone https://github.com/BakerBart/python-article-parser.git
    cd python-article-parser` 
    
3.  Install required dependencies:
    
    `pip install openai` 
    
4.  Ensure you have your OpenAI API key configured. Set it in your environment:
    
    `export OPENAI_API_KEY="your-api-key"`

---
## Usage
1.  Place the source text in `source_text.txt`.
2.  Run the application:

    `python main.py` 
    
3.  Outputs:
    -   Generated article HTML: `artykul.html`
    -   Complete preview: `podglad.html`

---
## Customizing the Template

-   Modify `szablon.html` to adjust the styling or structure of the preview template.

