
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split('\n')

#the maximum is 1313, but is you cannot go through this route. (the minimum is 266, just for curiosity)

int_triangle = []
path_index = []
soma = 0

for each in triangle:
	row = each.split(' ')
	list_row = []
	for n in row:
		list_row.append(int(n))
	int_triangle.append(list_row)

def find_route_within_triangle():
	global soma
	l = 0
	r = 0

	for each in int_triangle:
		#print(each[l], each[r])
		greater = 0
		greater_index = 0
		if each[l] >= each[r]:
			greater = each[l]
			greater_index = l
		else:
			greater = each[r]
			greater_index = r
		
		l = greater_index
		r = l + 1
		path_index.append(l)
		soma += greater

#i passed to much time on it, this is ai generated, i'm looking forward to understand this better.
def find_maximum_total(triangle):
    # Start from the second-to-last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Replace the current cell with the sum of itself and the max of the two below
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    # The top element now contains the maximum total
    return triangle[0][0]

def print_triangle_and_route(): 
	spaces = 15
	for row in int_triangle:
		for _ in range(spaces):
			print(" ", end="")
		spaces -= 1
		red_index = path_index.pop(0)
		for i, col in enumerate(row):
			if col < 10:
				print("0", end="")
			if(i == red_index):
				print("\033[31m" + str(col) + "\033[0m", end=" ")
			else:
				print(col, end=" ")
		print("")
	print("\nRoute sum = " + str(soma) + "\n")

find_route_within_triangle()
print_triangle_and_route()
print(find_maximum_total(int_triangle))
