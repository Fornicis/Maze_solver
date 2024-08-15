from tkinter import Tk, BOTH, Canvas

# Window class to create a GUI window with a canvas using Tkinter
class Window:
    def __init__(self, width, height):
        self.__root = Tk()  # Initialise the main window
        self.__root.title("Maze Solver")  # Set window title
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)  # Pack the canvas to fill the window
        self.__running = False  # Flag to control window loop
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Handle close button

    def redraw(self):
        self.__root.update_idletasks()  # Process GUI tasks
        self.__root.update()  # Update the window display

    def wait_for_close(self):
        self.__running = True  # Start the window loop
        while self.__running:
            self.redraw()  # Keep the window responsive
        print("window closed...")  # Message after window closes

    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)  # Draw the line on the canvas with the specified color


    def close(self):
        self.__running = False  # Stop the window loop

class Point:
    def __init__(self, x, y):
        self.x = x  # X-coordinate of the point
        self.y = y  # Y-coordinate of the point

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1  # Starting point of the line
        self.p2 = p2  # Ending point of the line

    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2
        )  # Draw the line on the canvas with the specified color and width
