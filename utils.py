import markdown
from xhtml2pdf import pisa
import io
import time

def generate_report_string(full_response: str, report: str, rationale: str) -> str:
    """
    Constructs the formatted Markdown string for the report.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Note: Emojis are removed from headers to ensure PDF font compatibility
    return f"""# KT Bot Route Analysis

**Date:** {timestamp}

## 1. AI Explanation
{full_response}

---

## 2. Executive Report
{report}

---

## 3. Technical Rationale
{rationale}
"""

def convert_markdown_to_pdf(markdown_content: str):
    """
    Converts a raw Markdown string into PDF bytes.
    Returns bytes if successful, None otherwise.
    """
    # 1. Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    
    # 2. Add basic CSS styling for a professional look
    styled_html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Helvetica, sans-serif; font-size: 12px; line-height: 1.5; }}
            h1 {{ color: #2E4053; font-size: 18px; border-bottom: 2px solid #2E4053; padding-bottom: 5px; }}
            h2 {{ color: #2874A6; font-size: 16px; margin-top: 20px; }}
            hr {{ border: 0; border-top: 1px solid #ddd; }}
            pre {{ background-color: #f4f6f7; padding: 10px; border-radius: 5px; font-family: monospace; }}
            strong {{ color: #17202A; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # 3. Generate PDF
    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(
        io.BytesIO(styled_html.encode("utf-8")), 
        dest=pdf_buffer
    )
    
    if pisa_status.err:
        return None
        
    return pdf_buffer.getvalue()