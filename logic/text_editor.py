from logic.commands import *
from logic.file import File
from logic.cursor import Cursor


class TextEditor:
    """
    This object is the abstraction of the text editor itself.
    It composes all of the individual logic together to form the representation
    of the text editor.
    """

    def __init__(self, file_path: str):
        self.__file = File(file_path)
        self.__cursor = Cursor(
            len(self.__file.get_file_contents()), len(self.__file.get_line(0))
        )

    def get_current_document_contents(self):
        return self.__file.get_file_contents()

    def move_cursor(self, row_movement: int, column_movement: int) -> None:
        self.__cursor.move_column(column_movement)
        self.__cursor.move_row(row_movement)
        self.__cursor.set_current_line_length(
            len(self.__file.get_line(self.__cursor.get_cursor_location()[0]))
        )

    def get_cursor_position(self):
        return (
            self.__cursor.get_cursor_location()[0],
            self.__cursor.get_cursor_location()[1],
        )

    def insert_new_line(self):
        self.__file.modify_contents(NewLine(), *self.__cursor.get_cursor_location())
        self.__clean_contents()
        self.__cursor.set_document_row_length(len(self.__file.get_file_contents()))
        self.move_cursor(1, 0)

    def __recurse_on_file_contents_delimiter(self, string, delimiter, temp_list ):
        try:
            n = string.index(delimiter)
            self.__recurse_on_file_contents_delimiter(string[0:n], delimiter, temp_list)
            self.__recurse_on_file_contents_delimiter(
                string[n + len(delimiter) :], delimiter, temp_list
            )
        except ValueError:
            temp_list.append(string)

    def __split_on_file_delimiter(self, delimiter: str, temp_list):
        temp_file_contents = self.__file.get_file_contents().copy()
        for line in temp_file_contents:
            self.__recurse_on_file_contents_delimiter(line, delimiter, temp_list)

    def __clean_contents(self) -> None:
        temp_list = []
        self.__split_on_file_delimiter("\n", temp_list)
        temp_list = list(map(str.rstrip, temp_list))
        self.__file.set_file_contents(temp_list)

    def save_file(self):
        self.__file.write_to_file()

    def __delete_line(self, i : int):
        temp=self.get_current_document_contents()
        temp.pop(i)
        self.__file.set_file_contents(temp)

    def delete_current_line(self):
        self.__file.modify_contents(
            DeleteLine(), self.__cursor.get_cursor_location()[0]
        )
        # deletes the now empty line
        if len(self.get_current_document_contents()) > 1:
            self.__delete_line(self.__cursor.get_cursor_location()[0])
        if self.__cursor.get_cursor_location()[0] >= len(self.__file.get_file_contents()):
            self.__cursor.move_row(-1)
        self.__cursor.set_document_row_length(len(self.__file.get_file_contents()))
        self.__cursor.set_current_line_length(len(self.__file.get_line(self.get_cursor_position()[0])))

    def write_character(self, char: str):
        if self.__cursor.get_insert_state() or len(self.__file.get_line(self.get_cursor_position()[0])) == 1:
            self.__file.modify_contents(Insert(), *self.__cursor.get_cursor_location(), char)
        else:
            self.__file.modify_contents(Insert(), self.__cursor.get_cursor_location()[0], self.__cursor.get_cursor_location()[1]+1, char)
        self.__cursor.set_current_line_length(len(self.__file.get_line(self.__cursor.get_cursor_location()[0])))
        self.__cursor.move_column(1)

    def remove_character(self):
        self.__cursor.move_column(-1)
        self.__file.modify_contents(Delete(), *self.__cursor.get_cursor_location())

    def get_insert_state(self):
        return self.__cursor.get_insert_state()
    
    def refresh(self):
        self.__cursor.set_document_row_length(len(self.__file.get_file_contents()))
        self.__cursor.set_current_line_length(len(self.__file.get_line(self.get_cursor_position()[0])))
        self.__cursor.check_bounds()
