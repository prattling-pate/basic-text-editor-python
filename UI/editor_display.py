from utility.logger import Logger
from logic.text_editor import TextEditor
from UI.keys import Keys
import curses
import sys


def run(stdscr) -> None:
    """Entry point into application"""

    file_path=sys.argv[1]

    logger = Logger("log.txt")

    stdscr.clear()

    running = True

    text_editor = TextEditor(file_path)

    logger.log("Text editor launched")

    while running:

        for i, line in enumerate(text_editor.get_current_document_contents(), 1):
            stdscr.addstr(f"{i}:{line}\n")

        stdscr.move(
            text_editor.get_cursor_position()[0],
            text_editor.get_cursor_position()[1]
            + len(str(text_editor.get_cursor_position()[0] + 1))
            + 1
        )

        user_input = stdscr.getch()

        logger.log("key pressed: " + str(user_input))

        if text_editor.get_insert_state():
            curses.curs_set(2)
        else:
            curses.curs_set(1)

        # match case used for special characters
        match(user_input):
            case curses.KEY_UP:
                text_editor.move_cursor(-1, 0)
            case curses.KEY_DOWN:
                text_editor.move_cursor(1, 0)
            case curses.KEY_LEFT:
                text_editor.move_cursor(0, -1)
            case curses.KEY_RIGHT:
                text_editor.move_cursor(0, 1)
            case Keys.DELETE:
                text_editor.delete_current_line()
            case Keys.BACKSPACE:
                text_editor.remove_character()
            case Keys.ESCAPE:
                running = False
            case Keys.ENTER:
                text_editor.insert_new_line()
            case Keys.TAB:
                text_editor.insert_tab()
            case Keys.BACK_TAB:
                text_editor.undo_tab()

        # else type in the normal character
        if chr(user_input).isascii():
            text_editor.write_character(chr(user_input))

        
        text_editor.refresh()

        logger.log(str(text_editor.get_current_document_contents()))
        logger.log(str(text_editor.get_cursor_position()))

        stdscr.clear()
        stdscr.refresh()

    text_editor.save_file()
    logger.log(f"File {file_path}")
    logger.log("Closing text editor")
    logger.write_log()


def start_editor():
    curses.wrapper(run)
