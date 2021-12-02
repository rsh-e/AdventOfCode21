## This is the second part of the Day 2 problem for the Advent oF Code challenge. To view the problem, you need to solve the first part to view this.
## Pretty much the same as the last problem, except you need to add a new variable aim and make 3 tweaks and you're set. I haven't thought of an alt solution.
## This will be documented in the near future

path = "Day2.txt"
test_path = "Day2Test.txt"

input_file = open(path, "r")

x_coordinate = 0
y_coordinate = 0
aim_value = 0

for line in input_file:
    a = line.split()
    if a[0] == "forward":
        forward_command = int(a[1])
        x_coordinate = x_coordinate + forward_command
        y_coordinate = y_coordinate + (aim_value * forward_command)

    elif a[0] == "up":
        up_command = int(a[1])
        aim_value = aim_value - up_command
        
    elif a[0] == "down":
        down_command = int(a[1])
        aim_value = aim_value + down_command

#print(x_coordinate)
#print(y_coordinate)

print(x_coordinate * y_coordinate)

#1842742223 is the answer
