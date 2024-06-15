from logic.commands import *
from logic.file import File
from logic.cursor import Cursor

class TextEditor:
    """
    This object is the abstraction of the text editor itself.
    It composes all of the individual logic together to form the representation
    of the text editor.
    """
    def __init__(self, file_path : str):
        self.__file = File(file_path)
        self.__cursor = Cursor(len(self.__file.get_file_contents()), len(self.__file.get_line(0)))
    
    def get_current_document_contents(self):
        return self.__file.get_file_contents()
    
    def move_cursor(self, row_movement : int, column_movement : int) -> None:
        self.__cursor.move_column(column_movement)
        self.__cursor.move_row(row_movement)
    
    def get_cursor_position(self):
        return self.__cursor.get_cursor_location()
