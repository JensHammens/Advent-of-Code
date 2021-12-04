import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input = open(os.path.join(location,'solutiondata')).read()
array = input.split("\n")

results = list(map(int, array))

increase = 0

for x in range(len(results)-1):
    y=x+1
    if(results[y]>results[x]):
        increase+=1

print(increase)