from collections import namedtuple
import json
from types import SimpleNamespace
from typing import Any

class ConsumeJSON():
    def __init__(self) -> None:
        pass

    def convert_json_to_obj(self, json_data) -> list:
        return json.loads(json_data, object_hook = lambda l: SimpleNamespace(**l))
        
    def standardize_json_format(self, type, json_data) -> list:
        """ ensure converted via convert_json_to_obj """
        if type == 'behave': 
            print("STANDARDIZE LIST HERE")