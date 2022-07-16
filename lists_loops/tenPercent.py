scoreList = []
scores = 0
for i in range (10):
    scores = float(input("enter a value "))
    tenPercent = (scores * .1) + scores
    scoreList.append(tenPercent)
print(scoreList)
