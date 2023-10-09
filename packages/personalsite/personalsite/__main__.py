import markdown2
import os

def read_page(page_name: str):
    md_file_path = f"./pages/{page_name}.md"
    assert os.path.exists(md_file_path)

    with open(md_file_path, "r") as file:
        md_content = file.read()
    html_content = markdown2.markdown(md_content)
    styled_html_content = f"""
    <html>
    <head>
        <title>Jack Latrobe - {page_name}</title>
        <style>
          body {{
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
              background-color: #f0f0f0;
          }}
          #content {{
              margin: 20px;
              padding-left: 10%;
              padding-right: 15%;
              max-width: 75%;
          }}
        </style>
    </head>
    <body>
        <div id="content">
            {html_content}
        </div>
    </body>
    </html>
    """
    return styled_html_content

def main(event):
  path = event.get("path", "index")
  content = read_page(path)
  return {
		"headers": {
			"Content-Type": "text/html"
		},
		"statusCode": 200,
		"body": content
	}
