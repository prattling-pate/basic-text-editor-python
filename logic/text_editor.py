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
        self._file = File(file_path)
        self._cursor = Cursor(
            len(self._file.get_file_contents()), len(self._file.get_line(0))
        )
        self._indent_size = 4

    def _get_current_line_length(self) -> int:
        lines = self.get_current_document_contents()
        cursor_row = self.get_cursor_position()[0]
        return len(lines[cursor_row])
    
    def _get_current_number_of_rows(self) -> int:
        return len(self.get_current_document_contents())
    
    def get_current_document_contents(self) -> list[str]:
        """
        Returns the file contents as a list of strings (each entry is a row).
        """
        return self._file.get_file_contents()

    def move_cursor(self, row_movement: int, column_movement: int) -> None:
        """
        Moves the cursor row_movement rows to the right and column_movement columns down.
        """
        self._cursor.move_column(column_movement)
        self._cursor.move_row(row_movement)
        self._cursor.set_current_line_length(self._get_current_line_length())

    def get_cursor_position(self) -> tuple[int, int]:
        return self._cursor.get_cursor_location()

    def insert_new_line(self) -> None:
        """
        Inserts a new line where the cursor is currently pointing
        """
        self._file.modify_contents(NewLine(), *self._cursor.get_cursor_location())
        temp_list = []
        for line in self.get_current_document_contents():
            temp_list += line.split("\n")
        self._file.set_file_contents(temp_list)
        self._cursor.set_document_row_length(self._get_current_number_of_rows())
        self.move_cursor(1, 0)

    def save_file(self) -> None:
        """
        Writes the stored file changes to the file associated to it.
        """
        self._file.write_to_file()

    def _delete_line(self, i: int) -> None:
        temp = self.get_current_document_contents()
        temp.pop(i)
        self._file.set_file_contents(temp)

    def delete_current_line(self) -> None:
        """
        Deletes the line that the cursor is currently pointing to.
        """
        self._file.modify_contents(
            DeleteLine(), self._cursor.get_cursor_location()[0]
        )
        if len(self.get_current_document_contents()) > 1:
            self._delete_line(self._cursor.get_cursor_location()[0])
        if self._cursor.get_cursor_location()[0] >= len(
            self._file.get_file_contents()
        ):
            self._cursor.move_row(-1)
        self._cursor.set_document_row_length(self._get_current_number_of_rows())
        self._cursor.set_current_line_length(self._get_current_line_length())

    def write_character(self, char: str) -> None:
        self._file.modify_contents(Insert(), *self._cursor.get_cursor_location(), char)
        self._cursor.set_current_line_length(self._get_current_line_length())
        self._cursor.move_column(1)

    def remove_character(self) -> None:
        self._cursor.move_column(-1)
        current_line = self.get_cursor_position()[0]
        if len(self._file.get_line(current_line)) == 0:
            self.delete_current_line()
        else:
            self._file.modify_contents(Delete(), *self._cursor.get_cursor_location())

    def get_insert_state(self) -> bool:
        return self._cursor.get_insert_state()

    def refresh(self) -> None:
        """
        Refreshes the stored length of the document and stored current line length
        """
        self._cursor.set_document_row_length(self._get_current_number_of_rows())
        self._cursor.set_current_line_length(self._get_current_line_length())
        self._cursor.bound_cursor()

    def insert_tab(self) -> None:
        for i in range(self._indent_size):
            self.write_character(" ")
