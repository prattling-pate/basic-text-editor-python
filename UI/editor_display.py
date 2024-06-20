from utility.logger import Logger
from logic.text_editor import TextEditor
from UI.keys import Keys
import curses
import sys


def display_editor(text_editor: TextEditor, stdscr: curses.window):
    for i, line in enumerate(text_editor.get_current_document_contents(), 1):
        stdscr.addstr(f"{i}:{line}\n")


def update_cursor(text_editor: TextEditor, stdscr: curses.window):
    current_row_visual, current_column_logical = text_editor.get_cursor_position()
    current_column_visual = (
        current_column_logical + len(str(text_editor.get_cursor_position()[0] + 1)) + 1
    )
    stdscr.move(current_row_visual, current_column_visual)


def display_documentation_instructions(screen: curses.window):
    screen.addstr("INSERT INSTRUCTIONS HERE")


def run(screen) -> None:
    """Entry point into application"""

    file_path = sys.argv[1]

    logger = Logger("log.txt")

    screen.clear()

    curses.noecho()

    curses.raw()

    running = True

    text_editor = TextEditor(file_path)

    logger.log("Text editor launched")

    while running:

        display_editor(text_editor, screen)

        display_documentation_instructions(screen)

        update_cursor(text_editor, screen)

        user_input = screen.getch()

        logger.log("key pressed: " + str(user_input))

        if text_editor.get_insert_state():
            curses.curs_set(2)
        else:
            curses.curs_set(1)

        # match case used for special characters
        match (user_input):
            case curses.KEY_UP:
                text_editor.move_cursor(-1, 0)
            case curses.KEY_DOWN:
                text_editor.move_cursor(1, 0)
            case curses.KEY_LEFT:
                text_editor.move_cursor(0, -1)
            case curses.KEY_RIGHT:
                text_editor.move_cursor(0, 1)
            case Keys.DELETE.value:
                text_editor.push_current_state_to_stack()
                text_editor.delete_current_line()
            case Keys.BACKSPACE.value:
                text_editor.push_current_state_to_stack()
                text_editor.remove_character()
            case Keys.ESCAPE.value:
                running = False
            case Keys.ENTER.value:
                text_editor.push_current_state_to_stack()
                text_editor.insert_new_line()
            case Keys.TAB.value:
                text_editor.push_current_state_to_stack()
                text_editor.insert_tab()
            case Keys.BACK_TAB.value:
                text_editor.push_current_state_to_stack()
                text_editor.undo_tab()
            case Keys.HOME.value:
                text_editor.move_cursor_to_beginning()
            case Keys.END.value:
                text_editor.move_cursor_to_end()
            case Keys.SHIFT_UP.value:
                text_editor.move_cursor(-1, 0, highlight=True)
            case Keys.SHIFT_DOWN.value:
                text_editor.move_cursor(1, 0, highlight=True)
            case Keys.SHIFT_LEFT.value:
                text_editor.move_cursor(0, -1, highlight=True)
            case Keys.SHIFT_RIGHT.value:
                text_editor.move_cursor(0, 1, highlight=True)
            case Keys.CTRL_C.value:
                text_editor.copy_to_clipboard()
            case Keys.CTRL_X.value:
                text_editor.push_current_state_to_stack()
                text_editor.cut_to_clipboard()
            case Keys.CTRL_V.value:
                text_editor.push_current_state_to_stack()
                text_editor.paste_clipboard_contents()
            case Keys.CTRL_Y.value:
                text_editor.redo_last_change()
            case Keys.CTRL_Z.value:
                text_editor.undo_last_change()
            case Keys.SHIFT_HOME.value:
                text_editor.move_cursor_to_beginning(highlight=True)
            case Keys.SHIFT_END.value:
                text_editor.move_cursor_to_end(highlight=True)
            case _:
                text_editor.push_current_state_to_stack()
                text_editor.write_character(chr(user_input))

        text_editor.refresh()

        logger.log(str(text_editor.get_current_document_contents()))
        logger.log(str(text_editor.get_cursor_position()))
        logger.write_log()

        screen.clear()
        screen.refresh()

    text_editor.save_file()
    logger.log(f"File {file_path}")
    logger.log("Closing text editor")
    logger.write_log()


def start_editor():
    curses.wrapper(run)
