import os
import time
from utils.prepare_prompt import PreparePrompts
from utils.generate import generate_output

class Agent():
    """
    An agent class that handles the process of preparing prompts and generating outputs
    using OpenAI's API based on user input.
    
    Attributes:
        name (str): Name of the agent
        openai_config (str): Configuration for OpenAI API, taken from `prompts` folder
        user_input (dict): Input provided by the user
        
    """
    
    def __init__(self, name:str, openai_config:str, user_input:dict):
        """
        Initializes the Agent with name, OpenAI configuration, and user input.
        
        Args:
            name (str): Name of the agent
            openai_config (str): Configuration for OpenAI API, taken from `prompts` folder
            user_input (dict): Input provided by the user
        """
        self.name = name
        self.openai_config = openai_config
        self.user_input = user_input
        
        # Print agent header
        print("=======================")
        print(f"{self.name}")
        print("=======================")

    def run(self):
        """
        Executes the agent's main workflow:
        1. Prepares prompts using PreparePrompts utility
        2. Generates output using generate_output utility
        3. Measures and reports execution time
        
        Returns:
            The generated output from the OpenAI API
        """
        print(f"-> {self.name}_Preparing Prompts")
        
        # Prepare prompts and parameters
        pr = PreparePrompts(openai_config=self.openai_config)
        messages, params = pr.prepare_prompts(user_input=self.user_input)
        
        # Generate output and measure time
        start_time = time.time()
        print(f"-> {self.name}_Generating Output")
        op = generate_output(message=messages, params=params)
        end_time = time.time()
        
        # Calculate and print elapsed time
        elapsed_time = end_time - start_time
        print(f"-> {self.name}_It took {elapsed_time:.2f} seconds to generate the output")
        
        return op