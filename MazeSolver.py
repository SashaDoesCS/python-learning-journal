def solve_maze(maze, x, y, exit_x, exit_y):
    try:
        # Base case: if we have reached the exit
        if x == exit_x and y == exit_y:
            maze[x][y] = 2  # Mark the exit as part of the solution path
            return True

        # Check if the current position is valid: within bounds and not a wall (1)
        if len(maze) > x >= 0 == maze[x][y] and 0 <= y < len(maze[0]):
            # Mark the current tile as part of the solution path
            maze[x][y] = 2

            # directions: right, down, left, up
            if solve_maze(maze, x + 1, y, exit_x, exit_y):  # right
                return True
            if solve_maze(maze, x, y + 1, exit_x, exit_y):  # down
                return True
            if solve_maze(maze, x - 1, y, exit_x, exit_y):  # left
                return True
            if solve_maze(maze, x, y - 1, exit_x, exit_y):  # up
                return True

            # If no direction works, backtrack: unmark the current tile
            maze[x][y] = 0
            return False

        # If the current tile is invalid (out of bounds or a wall), return False
        return False
    
    except IndexError:
        print(f"Error: Invalid index encountered at position ({x}, {y}).")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Example maze
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0]
]

start_x, start_y = 0, 1  # Starting position
exit_x, exit_y = 4, 4    # Exit position

if solve_maze(maze, start_x, start_y, exit_x, exit_y):
    print("Path found!")
else:
    print("No path found.")

# Printing the solution path (2 marks the path)
for row in maze:
    print(row)
