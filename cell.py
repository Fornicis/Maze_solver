from graphics import Line, Point

class Cell:
    def __init__(self, win):
        # Initialise a Cell object with default wall settings.
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        # Draw the walls of the cell based on its properties.
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Draw left wall if present, if not, draws a white line to indicate opening
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        # Draw top wall if present, if not, draws a white line to indicate opening
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        # Draw right wall if present, if not, draws a white line to indicate opening
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        # Draw bottom wall if present, if not, draws a white line to indicate opening
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        # Calculate the center of the current cell
        x_centre_start = (self._x1 + self._x2) // 2
        y_centre_start = (self._y1 + self._y2) // 2

        # Calculate the center of the destination cell
        x_centre_end = (to_cell._x1 + to_cell._x2) // 2
        y_centre_end = (to_cell._y1 + to_cell._y2) // 2

        # Set the line color based on whether the move is being undone
        fill_colour = "gray" if undo else "red"

        # Draw the line connecting the two cells
        line = Line(Point(x_centre_start, y_centre_start), Point(x_centre_end, y_centre_end))
        self._win.draw_line(line, fill_colour)
