import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input = open(os.path.join(location,'solutiondata.csv')).read()
array = input.split("\n")

results = list(map(int, array))

increase = 0

for x in range(len(results)-3):
    y=x+1
    z=x+2
    a=x+3
    numberA = results[x]+results[y]+results[z]
    numberB = results[y]+results[z]+results[a]

    if(numberB>numberA):
        increase+=1
        
print(increase)