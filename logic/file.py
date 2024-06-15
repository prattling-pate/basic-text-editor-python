from logic.commands import Command

class File:
    """Class representing the abstraction of a file in the text editor"""

    def __init__(self, file_path: str):
        self.__path : str = file_path
        self.__contents : list[str] = self.__fetch_file_contents()

    def __fetch_file_contents(self) -> list[str]:
        """Returns the contents of the file represented in object as a list of strings"""
        file_contents: list[str] = []
        try:
            with open(self.__path, "r") as file:
                file_contents = file.readlines()
        except IOError:
            print(f"cannot write to file @{self.__path}")
        return file_contents

    def write_to_file(self):
        """Writes current contents to file on disk"""
        with open(self.__path, "w") as file:
            file.writelines(self.__contents)

    def modify_contents(self,command : Command, line : int , *args) -> None:
        """
        Modifies the contents of the file given a line number and string index
        """
        self.__contents[line]=command.execute_command(self.__contents[line], *args)

    def get_line(self, line : int):
        return self.__contents[line]

    def get_file_contents(self) -> list[str]:
        return self.__contents
