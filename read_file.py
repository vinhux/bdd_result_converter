import json

class ReadFile:
    def __init__(self) -> None:
        pass

    def read_file_to_json(self, file_path) -> str:
        print(file_path)
        with open(file_path, 'r') as f:
            data = f.read()
        return data
        