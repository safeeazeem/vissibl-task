import os
import uuid
import argparse
import datetime
from config import config
from dotenv import load_dotenv
from utils.utils import read_text_file, write_to_file
from utils.convert_to_pdf import convert_report_to_pdf
from agent.agent import Agent

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function that orchestrates the process of populating company information
    into an ISO template form and validating the results.
    """
    
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="A program to populate company information into an ISO template form")

    # Define command-line arguments
    parser.add_argument("--company", type=str, help="The name of the company questionnaire file")
    parser.add_argument("--template", type=str, help="The name of the template to use.")

    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Construct file paths using the config module and provided arguments
    ISO_TEMPLATE_PATH = f"{config.TEMPLATE_PATH}/{args.template}"
    COMPANY_PATH = f"{config.COMPANY_INFORMATION_PATH}/{args.company}"
    
    # Generate a unique identifier for output files
    UNIQUE_UID = str(uuid.uuid4()).split('-')[0]
    
    # Get current datetime and format it for use in filenames
    dt = datetime.datetime.today().replace(microsecond=0)
    dt = "_".join(str(dt).split())
    
    # Print progress messages
    print("1. Reading ISO Template")
    iso_template = read_text_file(ISO_TEMPLATE_PATH)
    print("2. Reading Company information")
    company_information = read_text_file(COMPANY_PATH)

    # Define output file names with timestamp and unique ID
    OUTPUT_FILE_NAME = f"./output/{args.company[0:-4]}_{str(dt)}_{UNIQUE_UID}_output.txt"
    OUTPUT_FILE_VALIDATION_NAME_PDF = f"./output/{args.company[0:-4]}_{str(dt)}_{UNIQUE_UID}_validation_output_report.pdf"
    
    # Prepare input data for the Agent
    user_input = {
        "company_information": company_information,
        "iso_template": iso_template
    }

    # Create and run the Editor Agent to populate the template
    editor_agent = Agent(
        name="Editor Agent",
        openai_config="editor",
        user_input=user_input
    )
    op = editor_agent.run()

    # Write the populated template to a file
    write_to_file(
        filename=OUTPUT_FILE_NAME,
        text=op
    )
    
    # Prepare input for the Validator Agent
    user_input = {
        "company_information": company_information,
        "iso_template": iso_template,
        "completed_template": read_text_file(OUTPUT_FILE_NAME)
    }
    
    # Create and run the Validator Agent to validate the populated template
    validator_agent = Agent(
        name="Validator Agent",
        openai_config="validator",
        user_input=user_input
    )
    op = validator_agent.run()

    # Convert the validation report to PDF format
    convert_report_to_pdf(content=op, file_name=OUTPUT_FILE_VALIDATION_NAME_PDF)

if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()

