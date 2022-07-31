# * 1. number of stones input
# 2. String presenting colors on stones


numStones = int(input())
stones = input()
numOfStones = 0

# print("Stones:", stones)

for i in range(numStones):
    if i != len(stones) - 1:
        if stones[i] == "R" and stones[i+1] == "R":
            # stones.replace("RR", "R")
            numOfStones += 1
        elif stones[i] == "G" and stones[i+1] == "G":
            # stones.replace("GG", "G")
            numOfStones += 1
        elif stones[i] == "B" and stones[i+1] == "B":
            # stones.replace("BB", "B")
            numOfStones += 1


print(numOfStones)
