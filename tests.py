import unittest
from maze import Maze

# Define a test case class inheriting from unittest.TestCase
class Tests(unittest.TestCase):
    
    # Test the creation of cells in a maze with standard dimensions
    def test_maze_create_cells(self):
        num_cols = 12  # Set the number of columns for the maze
        num_rows = 10  # Set the number of rows for the maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)  # Create a Maze instance
        
        # Assert that the number of columns in the maze matches the expected value
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        
        # Assert that the number of rows in the first column matches the expected value
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    # Test the creation of cells in a larger maze
    def test_maze_create_cells_large(self):
        num_cols = 24  # Set a larger number of columns
        num_rows = 24  # Set a larger number of rows
        m1 = Maze(0, 0, num_cols, num_rows, 50, 50)  # Create a larger Maze instance
        
        # Assert that the number of columns in the maze matches the expected value
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        
        # Assert that the number of rows in the first column matches the expected value
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    # Test the creation of cells in a smaller maze
    def test_maze_create_cells_small(self):
        num_cols = 3  # Set a smaller number of columns
        num_rows = 3  # Set a smaller number of rows
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)  # Create a smaller Maze instance
        
        # Assert that the number of columns in the maze matches the expected value
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        
        # Assert that the number of rows in the first column matches the expected value
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    # Test the functionality of breaking entrance and exit walls in the maze
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12  # Set the number of columns for the maze
        num_rows = 10  # Set the number of rows for the maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)  # Create a Maze instance
        
        # Assert that the top wall of the entrance (top-left cell) is removed
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        
        # Assert that the bottom wall of the exit (bottom-right cell) is removed
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

# If this script is executed, run the unittests
if __name__ == "__main__":
    unittest.main()
