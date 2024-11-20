from logic.commands import Command


class File:
    """Class representing the abstraction of a file in the text editor"""

    def __init__(self, file_path: str):
        self._path: str = file_path
        self._contents: list[str] = self._fetch_file_contents()

    def _fetch_file_contents(self) -> list[str]:
        """Returns the contents of the file represented in object as a list of strings"""
        file_contents: list[str] = [""]
        try:
            with open(self._path, "r") as file:
                # used to strip newline characters
                file_contents = list(map(str.rstrip, file.readlines()))
                # prevents IndexError when file has nothing inside of it
                if len(file_contents) == 0:
                    file_contents.append("")
        except IOError:
            f = open(self._path, "x")
            f.write("")
            f.close()
        return file_contents

    def write_to_file(self) -> None:
        """Writes current contents to file on disk"""
        with open(self._path, "w") as file:
            for line in self._contents:
                file.write(line + "\n")

    def modify_contents(self, command: Command, line: int, *args) -> None:
        """Modifies the contents of the file given a line number and string index"""
        self._contents[line] = command.execute_command(self._contents[line], *args)

    def get_line(self, index: int) -> str:
        return self._contents[index]

    def set_line(self, index: int, new_line: str) -> None:
        self._contents[index] = new_line

    def get_file_contents(self) -> list[str]:
        return self._contents

    def set_file_contents(self, new_file_contents: list[str]) -> None:
        self._contents = new_file_contents
