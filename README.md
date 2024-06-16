# Python Text Editor

This is a basic terminal text editor which allows us to manipulate a given text file (or any other file that can be opened using some text encoding).

Using curses library to display to terminal, but all other logic is self made.

I will attempt to rewrite this in a more appropriate language later down the line.

## To do
1. Implement a system for representing a text file (abstraction of a text file) [Done-ish]
 - Might have to change from list -> tree/rope in order to optimise stuff
2. Implement a cursor which represents where in the text file a user is pointing to input to (abstraction of a cursor) [Done]
3. Implement a system for displaying this text file appropriately (i.e. every new line splits to a line break) [Done]
 - This may be possible with just print statements and clearing the terminal manually every update
4. Undo/Redo (Trees...) [TODO]
5. Search functionality [TODO]
6. Save file (Obviously) [Done-ish]
 - Need to auto-save or allow user to save themselves
7. Storing states between opening files (closing file doesn't remove the undo/redo trees, last cursor location etc.) [TODO]
 - Make this a seperate data object
8. Mouse support [TODO]
9. Custom binding for actions using a config file (.json, .ini, .cfg etc.) [TODO]

## Directory structure
1. UI classes/abstractions in one folder
2. Logical classes/abstractions in another folder
 - Data structures subfolder (trees)
 - Application structures subfolder
3. folder for metadata files (states of files are stored here)
4. Command interface for modifying text
 - Delete command
 - append command
 - replace command
