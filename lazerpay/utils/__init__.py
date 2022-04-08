from .constants import *

def validate_params(param1, param2):
    """
    Making sure any JSON/Dictonary
    Data contains the required keys

    :type param1: List
    :type param2: List
    """

    param1 = set(param1)
    param_not_present = param1.difference(set(param2))

    if param_not_present:
        raise Exception(f"Expected field(s) : { ', '.join(param_not_present) }")
        