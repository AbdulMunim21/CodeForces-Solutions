weights = input()
numYears = 0
condition = True
seperatedWeights = weights.split(" ")
limak = int(seperatedWeights[0])
bob = int(seperatedWeights[1])
while condition:
    if limak <= bob:
        limak = limak * 3
        bob = bob * 2
        numYears += 1
    else:
        condition = False

print(numYears)
