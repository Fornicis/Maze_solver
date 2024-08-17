from graphics import Window, Line, Point
from maze import Maze

def main():
    num_rows = 12  # Number of rows in the maze
    num_cols = 16  # Number of columns in the maze
    margin = 50  # Margin around the maze
    screen_x = 1024  # Width of the window
    screen_y = 768  # Height of the window

    # Calculate the size of each cell based on the screen size and margins
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)  # Create a window with the specified dimensions

    # Create a maze with the calculated parameters and draw it in the window
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 5074645)


    # Keep the window open until manually closed
    win.wait_for_close()

# Run the main function
main()
