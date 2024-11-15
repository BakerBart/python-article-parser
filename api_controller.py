from openai import OpenAI

def generate_html_with_openai(article_content):
  prompt = (
      "Analyze the following article text and generate its HTML representation, wrapped in <article> tag. Do not change the article content. Do not return any comments or additional text or tags."
      "Use appropriate HTML tags to structure the content, such as <h1>, <h2>, <p>, <ul>, and <li>. "
      "Identify logical sections and ensure proper header hierarchy. "
      "Suggest suitable places for images by including <img src=\"image_placeholder.jpg\" alt=\"Detailed image description - use 10-15 words, which can be used as a prompt to generate this image\"> "
      "and add captions under these images using a proper html tag. Wrap each image and caption inside a <figure> tag. "
      "Do not include any CSS or JavaScript. "
      "Return only the content that will be placed between <body> and </body> tags. Do not use <html>, <head> and <body> tags.\n\n"
      f"Article:\n{article_content}"
    )

  client = OpenAI()

  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
          "role": "system",
          "content": "You are an advanced programming assistant. Your primary objective is to deeply understand the expectations of a developer and generate precise, clean, and efficient code based on the provided instructions. You prioritize clarity, modularity, and best practices in coding. When responding, ensure you meet all specified requirements, address potential edge cases, and provide insightful explanations where needed. Focus on delivering solutions that are production-ready and adhere to modern programming standards."
        },
        {"role": "user", "content": prompt},
    ]
  )

  return response.choices[0].message.content