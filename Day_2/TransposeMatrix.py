X = [[12,7,7],[4,9 ,5],[3,9 ,8]]

res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       res[j][i] = X[i][j]

for r in res:
   print(r)
