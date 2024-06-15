from logic.text_editor import TextEditor
import logging
import curses

def run(stdscr) -> None:
    """Entry point into application"""
    stdscr.clear()

    running = True

    text_editor = TextEditor("pis2.txt")
    logger = logging.getLogger(__name__)

    while running:

        for i, line in enumerate(text_editor.get_current_document_contents(), 1):
            stdscr.addstr(f"{i}:{line}")

        stdscr.move(*(text_editor.get_cursor_position()))

        user_input = stdscr.getch()

        logger.info(str(stdscr.getyx()))

        if user_input == curses.KEY_UP:
            text_editor.move_cursor(-1, 0)
        elif user_input == curses.KEY_DOWN:
            text_editor.move_cursor(1, 0)
        elif user_input == curses.KEY_LEFT:
            text_editor.move_cursor(0, -1)
        elif user_input == curses.KEY_RIGHT:
            text_editor.move_cursor(0, 1)
        elif user_input == ord('x'):
            running = False
        
        stdscr.clear()
        stdscr.refresh()
    
    print("Exited")
    return

def start_editor():
    curses.wrapper(run)