import math

def distance(v1, v2):
    totalMan=0.0
    totalEuc=0.0
    for index in range(0, len(v1)):
        totalMan+=abs(v1[index]-v2[index])
        totalEuc+=abs((v1[index]-v2[index]))**2
    totalEuc = math.sqrt(totalEuc)

    return totalMan, totalEuc

vector1 = [13, 16, 23, 13]
vector2 = [10, 2, 25, 6]

print(distance(vector1, vector2))