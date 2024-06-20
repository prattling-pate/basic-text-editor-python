from utility.logger import Logger

class UndoRedoStack:
    def __init__(self):
        self._buffer_size = 50
        self._data = [[] for i in range(self._buffer_size)]
        self._back_pointer = -1
        self._front_pointer = -1

    def is_empty(self) -> bool:
        # logger = Logger("log_stack.txt")
        # logger.log(str(self._front_pointer))
        # logger.write_log()
        return self._front_pointer == -1 or self._front_pointer == self._back_pointer

    def _push(self, new_data):
        # fix back pointer to 0 once front pointer is greater than 1
        if self._front_pointer > 1 and self._back_pointer == -1:
            self._back_pointer = 0
        logger = Logger("log_stack.txt")
        logger.log(str(self._front_pointer))
        self._front_pointer = (self._front_pointer + 1) % self._buffer_size
        logger.log(str(self._front_pointer))
        if self._back_pointer == self._front_pointer:
            self._back_pointer += 1
        self._data[self._front_pointer] = new_data
        logger.log(str(self._data))
        logger.write_log()

    def _pop(self) -> list[str]:
        logger = Logger("log_stack.txt")
        logger.log(str(self.is_empty()))
        logger.write_log()
        if self.is_empty():
            raise StackUnderflowException()
        logger.log(str(self._front_pointer))
        front_point_element = self._data[self._front_pointer]
        self._front_pointer -= 1
        logger.write_log()
        return front_point_element

    def is_full(self):
        # logger = Logger("log_stack.txt")
        # logger.log(str((self._front_pointer + 1) % self._buffer_size == self._back_pointer))
        # logger.write_log()
        return (self._front_pointer + 1) % self._buffer_size == self._back_pointer

    def undo(self) -> list[str]:
        return self._pop()

    def add_state(self, state):
        self._push(state)

    def redo(self) -> list[str]:
        if self.is_full():
            raise StackOverflowException()
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