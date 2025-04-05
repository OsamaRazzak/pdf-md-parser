import os
from docling.document_converter import DocumentConverter

# Define the source PDF path
source = "data/Fund_Management_Reports_2014/November 2014.pdf"

# Convert the PDF to markdown
converter = DocumentConverter()
result = converter.convert(source)
final_result = result.document.export_to_markdown()  # Get markdown content

# Specify the output directory and file path
output_dir = "output"
output_file = os.path.join(output_dir, "November_2014_Report.md")

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Write the markdown content to the output file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(final_result)

print(f"Markdown content has been saved to {output_file}")
