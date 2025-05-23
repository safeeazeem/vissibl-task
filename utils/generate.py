import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_output(message:list, params:dict):
    """Sends an outbound request to OpenAI.

    Args:
        message (list): The prepared input
        params (dict): The parameters that are sent to OpenAI

    Returns:
        tuple: output and the price
    """
    client = OpenAI()

    try:
        response = client.chat.completions.create(
            
            model=params['model'],
            messages=message,
            temperature=params['temperature'],
            max_tokens=params['max_tokens'],
            top_p=params['top_p'],
        )
        response = response.to_dict()
        response = response['choices'][0]['message']['content']
        
        return response
    except Exception as e:
        raise Exception(e)