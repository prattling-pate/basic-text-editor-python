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
        """
        Returns the file contents as a list of strings (each entry is a row).
        """
        return self.__file.get_file_contents()

    def move_cursor(self, row_movement: int, column_movement: int) -> None:
        """
        Moves the cursor row_movement rows to the right and column_movement columns down.
        """
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
        """
        Inserts a new line where the cursor is currently pointing
        """
        self.__file.modify_contents(NewLine(), *self.__cursor.get_cursor_location())
        temp_list = []
        for line in self.get_current_document_contents():
            temp_list += line.split("\n")
        self.__file.set_file_contents(temp_list)
        self.__cursor.set_document_row_length(len(self.__file.get_file_contents()))
        self.move_cursor(1, 0)

    def save_file(self):
        """
        Writes the stored file changes to the file associated to it.
        """
        self.__file.write_to_file()

    def __delete_line(self, i: int):
        temp = self.get_current_document_contents()
        temp.pop(i)
        self.__file.set_file_contents(temp)

    def delete_current_line(self) -> None:
        """
        Deletes the line that the cursor is currently pointing to.
        """
        self.__file.modify_contents(
            DeleteLine(), self.__cursor.get_cursor_location()[0]
        )
        if len(self.get_current_document_contents()) > 1:
            self.__delete_line(self.__cursor.get_cursor_location()[0])
        if self.__cursor.get_cursor_location()[0] >= len(
            self.__file.get_file_contents()
        ):
            self.__cursor.move_row(-1)
        self.__cursor.set_document_row_length(len(self.__file.get_file_contents()))
        self.__cursor.set_current_line_length(
            len(self.__file.get_line(self.get_cursor_position()[0]))
        )

    def write_character(self, char: str) -> None:
        if (
            self.__cursor.get_insert_state()
            or len(self.__file.get_line(self.get_cursor_position()[0])) == 1
        ):
            self.__file.modify_contents(
                Insert(), *self.__cursor.get_cursor_location(), char
            )
        else:
            self.__file.modify_contents(
                Insert(),
                self.__cursor.get_cursor_location()[0],
                self.__cursor.get_cursor_location()[1] + 1,
                char,
            )
        self.__cursor.set_current_line_length(
            len(self.__file.get_line(self.__cursor.get_cursor_location()[0]))
        )
        self.__cursor.move_column(1)

    def remove_character(self) -> None:
        self.__cursor.move_column(-1)
        self.__file.modify_contents(Delete(), *self.__cursor.get_cursor_location())

    def get_insert_state(self) -> bool:
        return self.__cursor.get_insert_state()

    def refresh(self):
        """
        Refreshes the stored length of the document and stored current line length
        """
        row_length_of_document = len(self.__file.get_file_contents())
        current_line = self.get_cursor_position()[0]
        current_line_length = len(self.__file.get_line(current_line))
        self.__cursor.set_document_row_length(row_length_of_document)
        self.__cursor.set_current_line_length(current_line_length)
        self.__cursor.check_bounds()
