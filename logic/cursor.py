class Cursor:
    """Class representing a user's cursor"""
    def __init__(self, document_row_length : int, current_line_length : int) -> None:
        self.__column_number : int = 0
        self.__row_number : int = 0
        # insert dictates whether the cursor will 
        # replace the selected character or insert a character there
        self.__insert : bool = True
        self.__current_line_length : int = current_line_length
        self.__document_row_length : int = document_row_length

    def toggle_insert(self):
        self.__insert = not self.__insert
    
    def move_column(self, direction : int) -> None:
        """
        Move cursor right direction amount of times,
        if it reaches the bounds of the row it will not leave the row.
        """
        if (self.__column_number + direction < 0):
            self.__column_number = 0
            return
        elif (self.__column_number + direction >= self.__current_line_length):
            self.__column_number = self.__current_line_length - 1
            return
        self.__column_number += direction
    
    def move_row(self, direction : int) -> None:
        """
        Move cursor down direction amount of times,
        if it reaches the bounds of the document it will not leave the bounds.
        """
        if (self.__row_number + direction < 0):
            self.__row_number = 0
            return
        elif (self.__row_number + direction >= self.__document_row_length):
            self.__row_number = self.__document_row_length - 1
            return
        self.__row_number += direction

    def set_current_line_length(self, new_line_length):
        self.__current_line_length = new_line_length

    def get_cursor_location(self) -> tuple[int, int]:
        return (self.__row_number, self.__column_number)
