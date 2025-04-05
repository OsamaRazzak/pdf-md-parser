from llama_index.core import (
    SimpleDirectoryReader,
)
import os
from llama_parse import LlamaParse, ResultType
from llama_index.core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


def pre_processing(directory):
    folder_path = f"{directory}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    # Initialize LlamaParse with your API key
    parser = LlamaParse(
        result_type=ResultType.MD,  # Options: "markdown" or "text"
        verbose=True,
        num_workers=4,
        split_by_page=False,
        # use_vendor_multimodal_model=True,
        # vendor_multimodal_model_name="",
        # gpt4o_mode=True,
    )
    print(parser.api_key)

    # Define the file extractor for PDF files using LlamaParse
    file_extractor = {".pdf": parser}

    # Create a SimpleDirectoryReader to read files from the specified directory
    reader = SimpleDirectoryReader(
        "faq data/new_faqs_2025",
        file_extractor=file_extractor,
    )

    # Load data from the specified directory
    documents = reader.load_data()

    for index, doc in enumerate(documents):
        file_name = doc.metadata["file_name"]
        file_path = os.path.join(f"{directory}", file_name)
        print(f"file_path----------------------{file_path}")
        markdown_file_path = os.path.splitext(file_path)[0] + ".md"

        # Write the document's text content to the Markdown file
        with open(markdown_file_path, "w") as f:
            f.write(str(doc.text))
            print(f"Created Markdown file: {markdown_file_path}")

    return documents


directory = "faq_md"
docs = pre_processing(directory)
