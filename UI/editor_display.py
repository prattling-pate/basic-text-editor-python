from utility.logger import Logger
from logic.text_editor import TextEditor
import curses


def run(stdscr) -> None:
    """Entry point into application"""

    logger = Logger("log.txt")

    stdscr.clear()

    running = True

    file_path = "output.txt"

    text_editor = TextEditor(file_path)

    logger.log("Text editor launched")

    while running:

        for i, line in enumerate(text_editor.get_current_document_contents(), 1):
            stdscr.addstr(f"{i}:{line}")

        stdscr.move(*(text_editor.get_cursor_position()))

        user_input = stdscr.getch()

        logger.log("key pressed: " + str(user_input))

        if user_input == curses.KEY_UP:
            text_editor.move_cursor(-1, 0)
        elif user_input == curses.KEY_DOWN:
            text_editor.move_cursor(1, 0)
        elif user_input == curses.KEY_LEFT:
            text_editor.move_cursor(0, -1)
        elif user_input == curses.KEY_RIGHT:
            text_editor.move_cursor(0, 1)
        elif user_input == 330:
            text_editor.delete_current_line()
        elif user_input == 263:
            text_editor.remove_character()
        elif user_input == 27:
            running = False
        # enter key is equal to 10
        elif user_input == 10:
            text_editor.insert_new_line()
        elif chr(user_input).isalnum():
            text_editor.write_character(chr(user_input))

        stdscr.clear()
        stdscr.refresh()

    text_editor.save_file()
    logger.log(f"File {file_path}")
    logger.log("Closing text editor")
    logger.write_log()


def start_editor():
    curses.wrapper(run)
