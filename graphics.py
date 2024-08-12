from tkinter import Tk, BOTH, Canvas

# Window class to create a GUI window with a canvas using Tkinter
class Window:
    def __init__(self, width, height):
        self.__root = Tk()  # Initialize the main window
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

    def close(self):
        self.__running = False  # Stop the window loop
