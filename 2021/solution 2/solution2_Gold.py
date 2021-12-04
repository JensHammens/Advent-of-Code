import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input = open(os.path.join(location,'solutiondata')).read()
lines = input.split("\n")

depth = 0
horizontal = 0
aim = 0

for line in lines:
    parts = line.split(" ")
    direction = parts[0]
    if(direction == "forward"):
        horizontal+=int(parts[1])
        depth += aim*int(parts[1])
    if(direction == "down"):
        aim+=int(parts[1])
    if(direction == "up"):
        aim-=int(parts[1])
position = depth * horizontal
print(position)