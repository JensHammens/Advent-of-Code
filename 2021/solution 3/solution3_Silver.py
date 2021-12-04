import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input = open(os.path.join(location,'solutiondata')).read()
lines = input.split("\n")

gamma = ""
epsilon = ""
zero = 0

for i in range(len(lines[0])):
    for line in lines:
        if(line[i] == "0"):
            zero+=1
    if(zero>len(lines)/2):
        gamma+="0"
    else:
        gamma+="1"
    zero=0

for binary in gamma:
    if binary == '0':
        epsilon += '1' 
    else:
        epsilon += '0'

gamma = int(gamma,2)
epsilon = int(epsilon,2)
print(gamma*epsilon)