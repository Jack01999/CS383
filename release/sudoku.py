from constraint import *
import sys

def solve(board):
	problem = Problem()

	# Define the variables: 9 rows of 9 variables rangin in 1...9
	for i in range(1, 10):
	    problem.addVariables(range(i * 10 + 1, i * 10 + 10), range(1, 10))

	# Each row has different values
	for i in range(1, 10):
	    problem.addConstraint(AllDifferentConstraint(), range(i * 10 + 1, i * 10 + 10))

	# Each colum has different values
	for i in range(1, 10):
	    problem.addConstraint(AllDifferentConstraint(), range(10 + i, 100 + i, 10))

	# Each 3x3 box has different values
	problem.addConstraint(
	    AllDifferentConstraint(), [11, 12, 13, 21, 22, 23, 31, 32, 33]
	)
	problem.addConstraint(
	    AllDifferentConstraint(), [41, 42, 43, 51, 52, 53, 61, 62, 63]
	)
	problem.addConstraint(
	    AllDifferentConstraint(), [71, 72, 73, 81, 82, 83, 91, 92, 93]
	)

	problem.addConstraint(
	    AllDifferentConstraint(), [14, 15, 16, 24, 25, 26, 34, 35, 36]
	)
	problem.addConstraint(
	    AllDifferentConstraint(), [44, 45, 46, 54, 55, 56, 64, 65, 66]
	)
	problem.addConstraint(
	    AllDifferentConstraint(), [74, 75, 76, 84, 85, 86, 94, 95, 96]
	)

	problem.addConstraint(
	    AllDifferentConstraint(), [17, 18, 19, 27, 28, 29, 37, 38, 39]
	)
	problem.addConstraint(
	    AllDifferentConstraint(), [47, 48, 49, 57, 58, 59, 67, 68, 69]
	)
	problem.addConstraint(
	    AllDifferentConstraint(), [77, 78, 79, 87, 88, 89, 97, 98, 99]
	)

	# Some value is given.

	solution_counter = 0
	for i in range(1, 10):
	    for j in range(1, 10):
	        if board[i - 1][j - 1] != 0:
	            problem.addConstraint(
	                lambda var, val=board[i - 1][j - 1]: var == val, (i * 10 + j,)
	            )

	# Get the solutions.
	solutions = problem.getSolutions()
	return solutions


def main():
    # 21 solutions
    sudoku1 = [
    [0, 0, 4, 0, 3, 0, 0, 1, 0],
    [9, 0, 0, 5, 0, 0, 2, 4, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 4, 3, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 3, 7, 0, 0, 6, 0, 0, 9],
    [0, 6, 0, 0, 4, 0, 5, 0, 0],]

    # 1 solutions
    sudoku2 = [
    [0, 0, 4, 0, 3, 0, 0, 1, 0],
    [9, 0, 0, 5, 0, 0, 2, 4, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 3, 7, 0, 0, 6, 0, 0, 9],
    [0, 6, 0, 0, 4, 0, 5, 0, 0],]

    # 6 solutions
    sudoku3 = [
    [0, 0, 4, 0, 3, 0, 0, 1, 0],
    [9, 0, 0, 5, 0, 0, 2, 4, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 4, 7, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 3, 7, 0, 0, 6, 0, 0, 9],
    [0, 6, 0, 0, 4, 0, 5, 0, 0],]

    # 0 solutions
    sudoku4 = [
    [0, 0, 4, 0, 3, 0, 0, 1, 0],
    [9, 0, 0, 5, 0, 0, 2, 4, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 4, 6, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 3, 7, 0, 0, 6, 0, 0, 9],
    [0, 6, 0, 0, 4, 0, 5, 0, 0],]

    # 19 solutions
    sudoku5 = [
    [0, 0, 4, 0, 3, 0, 0, 1, 0],
    [9, 0, 0, 5, 0, 0, 2, 4, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 4, 8, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 3, 7, 0, 0, 6, 0, 0, 9],
    [0, 6, 0, 0, 4, 0, 5, 0, 0],]

    # 3 solutions
    sudoku6 = [
    [0, 0, 4, 0, 3, 0, 0, 1, 0],
    [9, 0, 0, 5, 0, 0, 2, 4, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 7, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 4, 9, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [5, 3, 7, 0, 0, 6, 0, 0, 9],
    [0, 6, 0, 0, 4, 0, 5, 0, 0],]

    myArr = [sudoku1, sudoku2, sudoku3, sudoku4, sudoku5, sudoku6]
    solution_counter = 0
    # Print the solutions
    for i in myArr:
        solutions = solve(i) 
        for solution in solutions:
            solution_counter += 1
        print(solution_counter)
        solution_counter = 0

if __name__ == "__main__":
    main()
   