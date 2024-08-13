from graphics import Window, Line, Point
from cell import Cell

def main():
    # Create a window with specified dimensions (800x600)
    win = Window(800, 600)  
    
    # Create the first cell, remove the right wall, and draw it at (50, 50) to (100, 100)
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    # Create the second cell, remove the left and bottom walls, and draw it at (100, 50) to (150, 100)
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    # Draw a move (line) between c1 and c2
    c1.draw_move(c2)

    # Create the third cell, remove the top and right walls, and draw it at (100, 100) to (150, 150)
    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    # Draw a move (line) between c2 and c3
    c2.draw_move(c3)

    # Create the fourth cell, remove the left wall, and draw it at (150, 100) to (200, 150)
    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    # Draw a move (line) between c3 and c4
    c3.draw_move(c4)

    # Keep the window open until manually closed
    win.wait_for_close()

# Run the main function
main()
