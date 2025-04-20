from utils.utils import load_config
from config import config

class PreparePrompts():
    """Class that prepares input prompts for LLM.
    """

    def __init__(self, openai_config):
        self.config_file = load_config(f"{config.PROMPTS_PATH}/{openai_config}.yaml")
        
        
    def prepare_prompts(self,user_input:dict):
        """The class method prepares the prompt that are fed to the LLM.
        It uses the config file and extracts relevant information from it.

        Args:
            user_input (dict): This is the input format for the LLM

        Returns:
            tuple: It returns the prepared data and params for the LLM
        """
        message = []
        # Read the config file
        config_file = self.config_file
        params = config_file['OPENAI_SETTINGS']
        
        # Extract different sections of the prompt
        VERSION = config_file["USE_VERSION"]

        if VERSION:
            if "MESSAGE" in config_file[VERSION]:
                message_prompt = config_file[VERSION]['MESSAGE']

                message.append({
                    "role":"system",
                    "content": message_prompt
                }    
                )

            prompt = config_file[VERSION]['PROMPT']

        # Replace Values
        
        
        message_prompt = message_prompt.format(**user_input)
        prompt = prompt.format(**user_input)
        
        
        message.append({
            "role":"user",
            "content": prompt
        }
        )

        return message, params