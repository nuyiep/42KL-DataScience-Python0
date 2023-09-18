import sys

def count_all(string):
	character_count = len(string)
	print("The text contains", character_count, "characters:")
	punctuation_chars = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	upper_count = 0
	lower_count = 0
	punct_count = 0
	space_count = 0
	digit_count = 0
	for char in string:
		if char.isupper():
			upper_count += 1
		if char.islower():
			lower_count += 1
		if char in punctuation_chars:
			punct_count += 1
		if char.isspace():
			space_count += 1
		if char.isdigit():
			digit_count += 1
	print(upper_count, "upper letters")
	print(lower_count, "lower letters")
	print(punct_count, "punctuation marks")
	print(space_count, "spaces")
	print(digit_count, "digits")


def main():
	if (len(sys.argv) > 2):
		print("AssertionError: more than one argument is provided")
		sys.exit()
	if (len(sys.argv) < 2):
		user_input = input("What is the text to count? ")
		print(user_input)
		count_all(user_input + "\n")
	else:
		count_all(sys.argv[1])
	

if __name__ == "__main__":
	main()

# \r carriage return
# \n control d