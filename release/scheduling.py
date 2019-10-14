from constraint import *

def solve():
	problem = Problem()

	# Add all the class requirements
	problem.addVariables(["Air"], [234, 248, 234, 388, 622, 457]) 
	problem.addVariables(["Adversarial"], [388, 622, 400]) 
	problem.addVariables(["Core"], [457, 383]) 
	# Malicious requirement completed from 635

	# Create constraints
	problem.addConstraint(NotInSetConstraint([457]), ["Air"]) # Since Barry Otter is not allowed to take 622, there is no reason for him to take 457 for his Air Requirement
	problem.addConstraint(NotInSetConstraint([388, 622, 635])) # Barry Otter has completed 635, so he is also prohibited to take 388 and 622. Class 457 is also removed because it has to be taken next to 622 (Which he is prohibited from taking)
	problem.addConstraint(NotInSetConstraint([234, 126])) # Barry Otter has completed 234, so he is also prohibited to take 126
	solutions = problem.getSolutions()
	return solutions


def main():
	solutions = solve()
	solution_counter = 0
	for solution in solutions:
		solution_counter += 1
	print(solution_counter)

if __name__ == "__main__":
    main()
   