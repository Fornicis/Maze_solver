from graphics import Line, Point

class Cell:
    def __init__(self, win):
        # Initialize a Cell object with default wall settings.
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
        # Draw the walls of the cell based on its properties.
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Draw left wall if present
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)

        # Draw top wall if present
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)

        # Draw right wall if present
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)

        # Draw bottom wall if present
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
