# shared/utils.py

def validate_input(data):
    """
    Validate input data (example utility function).
    """
    if not isinstance(data, str):
        raise ValueError("Input must be a string")
    return data