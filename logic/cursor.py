class Cursor:
    """Class representing a user's cursor"""

    def __init__(self, document_row_length: int, current_line_length: int) -> None:
        self._column_number: int = 0
        self._row_number: int = 0
        self._current_line_length: int = current_line_length + 1
        self._document_row_length: int = document_row_length

    def move_column(self, direction: int) -> None:
        """
        Move cursor right direction amount of times,
        if it reaches the bounds of the row it will not leave the row.
        """
        if self._column_number + direction < 0:
            self._column_number = 0
            return
        elif self._column_number + direction >= self._current_line_length:
            self._column_number = self._current_line_length - 1
            return
        self._column_number += direction

    def move_row(self, direction: int) -> None:
        """
        Move cursor down direction amount of times,
        if it reaches the bounds of the document it will not leave the bounds.
        """
        if self._row_number + direction < 0:
            self._row_number = 0
            return
        elif self._row_number + direction >= self._document_row_length:
            self._row_number = self._document_row_length - 1
            return
        self._row_number += direction

    def set_current_line_length(self, new_line_length: int) -> None:
        self._current_line_length = new_line_length + 1

    def get_cursor_location(self) -> tuple[int, int]:
        return (self._row_number, self._column_number)

    def set_document_row_length(self, new_row_length: int) -> None:
        self._document_row_length = new_row_length

    def bound_cursor(self) -> None:
        """
        Checks bounds on cursor (fixes out of bounds)
        """
        if self._row_number < 0:
            self._row_number = 0
        elif self._row_number >= self._document_row_length:
            self._row_number = self._document_row_length - 1
        if self._column_number < 0:
            self._column_number = 0
        elif self._column_number >= self._current_line_length:
            self._column_number = self._current_line_length - 1

    def set_column(self, column: int):
        self._column_number = column
