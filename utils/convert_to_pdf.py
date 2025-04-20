
import markdown
from weasyprint import HTML
def convert_report_to_pdf(content: str, file_name: str):
    """
    Converts a markdown-formatted report to a PDF file with custom styling.
    
    Args:
        content (str): The markdown content to be converted to PDF
        file_name (str): The output filename/path for the PDF file
    """
    print("-> Converting Report to PDF")
   
    html_content = markdown.markdown(content, extensions=['tables'])

    # HTML document with custom styling that wraps the converted markdown content
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        body {{
            background: #e3eefa;
            border-left: 4px solid #1a4a7a;
            padding: 18px 24px;
            margin-bottom: 24px;
        }}
            h2, h3, h4 {{
                color: #1a4a7a;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                font-family: Arial, sans-serif;
                font-size: 15px;
                margin: 20px 0;
                background: #fff;
            }}
            th, td {{
                border: 1px solid #b0b0b0;
                padding: 8px 10px;
                text-align: left;
            }}
            th {{
                background: #e3eefa;
                color: #ffffff;
                font-weight: bold;background-color: #003366;
                color: #ffffff;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
            background-color: #f6f8fa;
            }}
            tr:nth-child(odd) {{
            background-color: #ffffff;
            }}
            td {{
            vertical-align: top;
        }}
            td:contains("Issue") {{
            color: #b30000;
            font-weight: bold;
            }}
            td:contains("No Issue") {{
            color: #228B22;
            font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>Validation Report</h1>
        {html_content}
    </body>
    </html>
    """
    HTML(string=full_html).write_pdf(file_name)