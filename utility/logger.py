from logic.file import File
from logic.commands import Append

class Logger:
    def __init__(self, file_path):
        self.__file = File(file_path)
    
    def log(self, to_log : str):
        self.__file.modify_contents(Append(), -1 , to_log)

    def write_log(self):
        self.__file.write_to_file()
