import sys

BOLD_RED = "\033[1;31m"
RESET = "\033[0m"

# Function to get the total number of lines in the pyramid
def get_total_lines(height: int) -> int:
    total_lines = 0
    for i in range(height):
        total_lines += i + 3
    return total_lines

def print_line(num_spaces: int, num_stars: int) -> None:
    print(" " * num_spaces, end="")
    print("/", end="")
    print("*" * num_stars, end="")
    print("\\", end="")
    print()

def	get_first_line_spaces(height: int) -> int:
	spaces = 2
	increment = 6
	for i in range(height - 1):
		spaces += increment
		if i % 2 == 0:
			increment += 1
		else:
			increment += 2
	return spaces

# Affiche tous les arguments passés au programme sastantua.py
if len(sys.argv) != 2:
    if len(sys.argv) == 1:
        print(BOLD_RED + "Error: missing argument" + RESET)
    else:
        print(BOLD_RED + "Error: too many arguments" + RESET)
    exit(1)

# Check if the argument is a valid integer
try:
    height = int(sys.argv[1])
except ValueError:
    print(BOLD_RED + "Error: invalid argument" + RESET)
    exit(1)

height = int(sys.argv[1])
stage = 3
num_spaces = get_first_line_spaces(height)
num_stars = 1
add_stars = 2
remove_spaces = 2
print(get_first_line_spaces(height))

for i in range(height):
	for j in range(stage):
		print_line(num_spaces, num_stars)
		num_stars += 2
		num_spaces -= 1
	if i % 2 == 0:
		add_stars += 2
		if i != 0:
			remove_spaces += 1
	num_stars += add_stars
	num_spaces -= remove_spaces
	stage += 1

# 2: 2
# 3: 2
# 4: 3
# 5: 3
# 6: 4
# 7: 4
# 8: 5
# 9: 5
# 10: 6
# 11: 6
# 12: 7
# 13: 7
# 14: 8
# 15: 8
# 16: 9
# 17: 9
# 18: 10
# 19: 10
# 20: 11
# 21: 11

# x / 2 + 2

# Number stages: 1, Total lines : 3, spaces first line : 2
# Number stages: 2, Total lines : 7, spaces first line : 8
# Number stages: 3, Total lines : 12, spaces first line : 15
# Number stages: 4, Total lines : 18, spaces first line : 24
# Number stages: 5, Total lines : 25, spaces first line : 34
# Number stages: 6, Total lines : 33, spaces first line : 46
# Number stages: 7, Total lines : 42, spaces first line : 59
# Number stages: 8, Total lines : 52, spaces first line : 74
# Number stages: 9, Total lines : 63, spaces first line : 90
# Number stages: 10, Total lines : 75, spaces first line : 108
# Number stages: 11, Total lines : 88, spaces first line : 127
# Number stages: 12, Total lines : 102, spaces first line : 148
# Number stages: 13, Total lines : 117, spaces first line : 170
# Number stages: 14, Total lines : 133, spaces first line : 194
# Number stages: 15, Total lines : 150, spaces first line : 219
# Number stages: 16, Total lines : 168, spaces first line : 246
