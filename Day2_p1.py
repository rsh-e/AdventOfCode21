## This is the solution to the 2nd day of the Advent of Code challenge found here: https://adventofcode.com/2021/day/2
## This is the solution the first part of the challenege. It will be documented in the near future.
## The lines of code I commented out is an alt solution to the challenge. I don't know which is more effiecient but yes, 2 different wqays to solve the problem.

path = "Day2.txt"
test_path = "Day2Test.txt"

input_file = open(path, "r")

#forward_values = []
#up_values = []
#down_values = []

x_coordinate = 0
y_coordinate = 0

for line in input_file:
    a = line.split()
    if a[0] == "forward":
        forward_command = int(a[1])
        #forward_values.append(forward_command)
        x_coordinate = x_coordinate + forward_command

    elif a[0] == "up":
        up_command = int(a[1])
        #up_values.append(up_command)
        y_coordinate = y_coordinate - up_command
        
    elif a[0] == "down":
        down_command = int(a[1])
        #down_values.append(down_command)
        y_coordinate = y_coordinate + down_command
    
#x_coordinate = sum(forward_values)
#y_coordinate = sum(down_values) - sum(up_values)

print(x_coordinate * y_coordinate)

# The answer is 2150351
