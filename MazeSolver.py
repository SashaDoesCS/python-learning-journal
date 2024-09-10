def solve_maze(maze, x, y, exit_x, exit_y):
    try:
        # Check if the current position is valid: within bounds and not a wall (1)
        # Ensure we are within bounds and the position is a valid path (0)
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            # Mark the current tile as part of the solution path
            maze[x][y] = 2

            # Step 3: Check if the current position is the exit
            if x == exit_x and y == exit_y:
                return True

            # Step 4: Explore the adjacent tiles recursively
            if solve_maze(maze, x + 1, y, exit_x, exit_y):  # right
                return True
            if solve_maze(maze, x, y + 1, exit_x, exit_y):  # down
                return True
            if solve_maze(maze, x - 1, y, exit_x, exit_y):  # left
                return True
            if solve_maze(maze, x, y - 1, exit_x, exit_y):  # up
                return True

            # Step 5: If no direction works, backtrack by unmarking the current tile
            maze[x][y] = 0
            return False

        # If the current tile is invalid (out of bounds, a wall, or already visited), return False
        return False

    except IndexError:  # catches errors and ensures the program doesn't throw exceptions
        print(f"Error: Invalid index encountered at position ({x}, {y}).")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# Test maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1]
]

start_x, start_y = 1, 1  # Starting position
exit_x, exit_y = 6, 6  # Exit position

# [1, 0, 1, 1, 1],
# [1, 0, 0, 1, 1],
# [1, 1, 0, 1, 1],
# [1, 0, 0, 0, 1],
# [1, 1, 1, 0, 0]
# start_x, start_y = 0, 1  # Starting position
# exit_x, exit_y = 4, 4  # Exit position
# base 6 by 6 example used to test


# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 0, 1, 0, 0, 0, 1, 1],
# [1, 0, 1, 0, 1, 0, 0, 1],
# [1, 0, 0, 0, 1, 1, 0, 1],
# [1, 1, 1, 0, 1, 0, 0, 1],
# [1, 0, 0, 0, 0, 1, 0, 1],
# [1, 1, 1, 1, 0, 1, 0, 1],
# [1, 1, 1, 1, 0, 0, 0, 1]
# start_x, start_y = 1, 1  # Starting position
# exit_x, exit_y = 6, 6  # Exit position
# 8 by 8 example

# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 0, 1, 0, 0, 0, 1, 1],
# [1, 0, 1, 0, 1, 0, 0, 1],
# [1, 0, 0, 0, 1, 1, 0, 1],
# [1, 1, 1, 0, 1, 0, 0, 1],
# [1, 0, 0, 0, 0, 1, 0, 1],
# [1, 1, 1, 1, 0, 1, 1, 1],
# [1, 1, 1, 1, 0, 0, 0, 1]
# start_x, start_y = 1, 1  # Starting position
# exit_x, exit_y = 6, 6  # Exit position
# 8 by 8 example


#     [1, 0, 0, 1, 1, 1, 1],
#     [1, 1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 0, 0]

# start_x, start_y = 0, 1  # Starting position
# exit_x, exit_y = 2, 6  # Exit position
# irregular map size example, 7 by 3


# Solve the maze
if solve_maze(maze, start_x, start_y, exit_x, exit_y):
    print("Path found!")
else:
    print("No path found.")

# Print the solution path (2 marks the path)
for row in maze:
    print(row)
