from graphics import Window, Line, Point

def main():
    win = Window(800, 600)  # Create a window with specified dimensions
    l = Line(Point(60, 100), Point(60, 400))  # Create a line from (60, 60) to (450, 450)
    win.draw_line(l, "black")  # Draw the line in black on the window's canvas
    win.wait_for_close()  # Keep the window open until manually closed

main()
