# Define the NQueens class
class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_backtracking(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_backtracking(row + 1)
                self.board[row] = -1  # Backtrack

        return False

    def solve_branch_and_bound(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve_branch_and_bound(row + 1):
                    return True
                self.board[row] = -1  # Backtrack

        return False

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                line = ['.'] * self.n
                line[row] = 'Q'
                print(' '.join(line))
            print()

# Create an instance of NQueens for 4x4 chessboard
n_queens = NQueens(8)

# Solve using backtracking
print("Solutions using backtracking:")
n_queens.solve_backtracking()
n_queens.print_solutions()

# Reset solutions for branch and bound
n_queens.solutions = []

# Solve using branch and bound
print("Solutions using branch and bound:")
n_queens.solve_branch_and_bound()
n_queens.print_solutions()
