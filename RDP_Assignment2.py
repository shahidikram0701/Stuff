def main():

    # grammar
    # S -> aSa | aa

	stack = []

	#print("START")
	inp = input("Enter a string to parse - ")
	index = 0
	matched_string = ""

	def print_stack(a):
		print("  |  ", end = "")
		for i in a:
			print(i, end = "  |  ")
		print()

	def match(term):
		nonlocal index
		nonlocal matched_string
		if(index < len(inp) and term == inp[index]):
			index += 1
			matched_string += 'a'
			print("\nMatched String : ", matched_string, end = "\n\n")
			return True
		else:
			return False

	def S():
		nonlocal index
		nonlocal matched_string
		prev_index = index
		prev_match = matched_string
		stack.append("S -> aSa")
		if(S1()):
			return True
		else:
			index = prev_index
			matched_string = prev_match
			stack.append("S -> aa")
			return S2()

	def S1():
        # match a and then call S then after it returns match a
        # returns True or False
		print("*" * 90)
		print()
		print("aSa rule expanded.....\n")
		print_stack(stack)
		if(match('a')):
			if(S()):
				if(match('a')):
					stack.pop()
					return True
		print("\nBackTrack", end = "\t")
		print(stack.pop(), end = "\n\n")
		print_stack(stack)
		print()
		return False

	def S2():
        # match aa and return status
        # returns True or False
		print("*" * 90)
		print()
		print("aa rule expanded....\n")
		print_stack(stack)
		if(match('a')):
			if(match('a')):
				stack.pop()
				return True

		print("\nBackTrack", end = "\t")
		print(stack.pop(), end = "\n\n")
		print_stack(stack)
		print()
		return False

	status = S() # String parsed successfully or not
	if(status and index == len(inp)):
		print("\n\n\tSTRING PARSED SUCCESSFULLY!!!!\n")
	else:
		print("\n\n\tSTRING PARSING FAILED!!!!\n")



if __name__ == "__main__":
    main()
