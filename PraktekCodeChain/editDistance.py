import numpy as np

def levenshteinDistance(s,t,ratioCalc = False):
    rows = len(s)+1
    col = len(t)+1
    distance = np.zeros((rows,col), dtype=int)

    for i in range(1,rows):
        for k in range(1, col):
            distance[i][0]=i
            distance[0][k]=k

    for col in range(1,col):
        for row in range(1,rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                if ratioCalc==True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col]= min(distance[row-1][col]+1,
                                distance[row][col-1]+1,
                                distance[row-1][col-1]+cost)
    if ratioCalc == True:
        Ratio = ((len(s)+len(t))-distance[row][col]) / (len(s)+len(t))
        return Ratio        
    else:
        return "The string are {} edits away".format(distance[row][col])

# str1="1234"
# str2="1034"

# print("Kalimat pertama= "+str1)
# print("Kalimat kedua= "+str2)
# Distance = levenshteinDistance(str1,str2)
# print(Distance)

# Ratios = levenshteinDistance(str1,str2,True)
# print("Persentase kemiripan antara kedua string"+str(Ratios))