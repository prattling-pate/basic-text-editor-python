from utility.logger import Logger


class UndoRedoStack:
    """
    Stack which implements circular queue ideas to create a buffer for undoing/redoing states of the program.
    Front pointer points to the current state of the program
    """
    def __init__(self):
        self._buffer_size = 50
        self._data = [[] for i in range(self._buffer_size)]
        self._back_pointer = -1
        self._front_pointer = -1

    def is_empty(self) -> bool:
        return self._front_pointer == -1 or self._front_pointer == self._back_pointer

    def _push(self, new_data):
        # fix back pointer to 0 once front pointer is greater than 1
        if self._front_pointer > 1 and self._back_pointer == -1:
            self._back_pointer = 0
        self._front_pointer = (self._front_pointer + 1) % self._buffer_size
        if self._back_pointer == self._front_pointer:
            self._back_pointer = (self._back_pointer + 1) % self._buffer_size
        self._data[self._front_pointer] = new_data

    def is_full(self):
        return (self._front_pointer + 1) % self._buffer_size == self._back_pointer

    def undo(self) -> list[str]:
        if self.is_empty():
            raise StackUnderflowException()
        if self._data[(self._front_pointer - 1) % self._buffer_size] == []:
            raise NoPastStateException()
        self._front_pointer = (self._front_pointer - 1) % self._buffer_size
        front_point_element = self._data[self._front_pointer]
        return front_point_element

    def add_state(self, state):
        self._push(state)

    def redo(self) -> list[str]:
        if self.is_full():
            raise StackOverflowException()
        if self._data[(self._front_pointer + 1) % self._buffer_size] == []:
            raise NoFutureStateException()
        self._front_pointer = (self._front_pointer + 1) % self._buffer_size
        return self._data[self._front_pointer]

    def __repr__(self) -> str:
        return str(self._data)


class StackOverflowException(Exception):
    def __init__(self, *args):
        super().__init__(self, *args)


class StackUnderflowException(Exception):
    def __init__(self, *args):
        super().__init__(self, *args)

class NoFutureStateException(Exception):
    def __init__(self, *args):
        super().__init__(self, *args)

class NoPastStateException(Exception):
    def __init__(self, *args):
        super().__init__(self, *args)
