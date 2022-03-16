VALID_CELL = 1


class PathFinder:
    def __init__(self, grid):
        """ The grid must be nxn two-dimensional array """
        self.grid = grid
        self.size = len(grid)

    def get_single_path(self, start, end):
        """
        Returns an array with possible paths
        :param start: List with start coordinates
        :type start: List[Tuple]
        :param end: List with end coordinates
        :type end: List[Tuple]
        """
        path = [start]
        last_position = start  # type: (int, int)
        current_position = start  # type: (int, int)
        path_found = False

        i = 0
        while not path_found:
            moves = self._get_possible_movements(current_position)

            # print(i)
            # print(moves)
            # print('last', last_position, 'current', current_position)
            for move in moves:
                # Ignore the previous position
                if move != last_position:
                    last_position = current_position
                    current_position = move
                    path.append(current_position)
                    # print(path)
                    # print()
                    break

            # Found the path
            if current_position == end:
                path_found = True

            i += 1

        return path

        # print(path)

    def _get_possible_movements(self, point):
        moves = []
        i = point[0]
        j = point[1]

        # Up
        if i - 1 >= 0 and self.grid[i - 1][j] == VALID_CELL:
            moves.append((i - 1, j))

        # Right
        if j + 1 < self.size and self.grid[i][j + 1] == VALID_CELL:
            moves.append((i, j + 1))

        # Down
        if i + 1 < self.size and self.grid[i + 1][j] == VALID_CELL:
            moves.append((i + 1, j))

        # Left
        if j - 1 >= 0 and self.grid[i][j - 1] == VALID_CELL:
            moves.append((i, j - 1))

        return moves
