import argparse
from markitdown import MarkItDown
from utils.utils import write_to_file

def convert_to_markdown(file_path:str):
    """
    Convert a given file (PDF, Docx, XLS) to markdown format.
    
    Args:
        file_path (str): Path to the input file to be converted
        
    Returns:
        The converted markdown content as text
    """
    # Initialize MarkItDown converter with plugins disabled
    md = MarkItDown(enable_plugins=False)  # Set to True to enable plugins
    # Convert the file and get the result
    result = md.convert(file_path)
    # Return the text content of the conversion
    return result.text_content

def main():
    """
    Main function that handles command-line arguments and executes the conversion.
    """
    # Set up argument parser with description
    parser = argparse.ArgumentParser(description="A program to convert PDF, Docx, XLS to markdown using Microsoft Markitdown.")

    # Define command-line arguments
    parser.add_argument("--input", type=str, help="The location of the input file")
    parser.add_argument("--output", type=str, help="The name of the output file")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Define output file path in the 'converted' directory with .txt extension
    OUTPUT_FILE_PATH = f"./converted/{args.output}.txt"

    # Print conversion message
    print(f"-> Converting \'{args.input}\' to markdown")
    # Convert the input file to markdown
    converted_md = convert_to_markdown(file_path=args.input)

    # Write the converted markdown to the output file
    write_to_file(
        filename=OUTPUT_FILE_PATH,
        text=converted_md
        )
    
# Standard Python idiom to execute main() when script is run directly
if __name__ == "__main__":
    main()
