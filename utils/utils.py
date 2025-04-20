import yaml
from markitdown import MarkItDown
# ======================================================================
# LOADING CONFIG VARIABLES
# ======================================================================
def load_config(config_file: str) -> dict:
    """Loading the prompt configuration

    Args:
        config_file (str): Path of the config file.

    Returns:
        dict: The loaded config file as dict.
    """
    with open(config_file) as f:
        config_file = yaml.safe_load(f)

    return config_file



# ======================================================================
# READ TEXT FILE
# ======================================================================
def read_text_file(file_path:str):
    """
    Reads a text file and returns its contents as a string.
    
    Parameters:
        file_path (str): The path to the text file to be read.
    
    Returns:
        str: The contents of the text file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")
# ======================================================================
# READ TEXT FILE
# ======================================================================
def write_to_file(filename:str, text:str):
    """
    Writes the given text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
        append (bool, optional): If True, appends to the file.
            If False (default), overwrites the file.
    """
    try:
        # Determine the write mode based on the append argument

        # Open the file in the specified mode
        with open(filename, "w") as file:
            # Write the text to the file
            file.write(text)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")
