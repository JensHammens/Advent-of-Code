import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input = open(os.path.join(location,'solutiondata')).read()
lineso = input.split("\n")
linesco2 = lineso

zero=0

for i in range(len(lineso[0])):
    for line in lineso:
        if(line[i] == "0"):
            zero+=1
    if(zero>len(lineso)/2):
        datahold="0"
    else:
        datahold="1"
    zero=0
    lineso = list(filter(lambda line: line[i] == datahold, lineso))
    if(len(linesco2)==1):
        break;
oxygen = lineso[0]

for i in range(len(linesco2[0])):
    for line in linesco2:
        if(line[i] == "0"):
            zero+=1
    if(zero<=len(linesco2)/2):
        datahold="0"
    else:
        datahold="1"
    zero=0
    linesco2 = list(filter(lambda line: line[i] == datahold, linesco2))
    if(len(linesco2)==1):
        break;
co2 = linesco2[0]

oxygen = int(oxygen,2)
co2 = int(co2,2)
print(oxygen*co2)