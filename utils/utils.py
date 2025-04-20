import yaml
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