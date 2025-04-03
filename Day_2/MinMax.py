a=[[1,2,3,5,8,8],[8,3,2,3]]
min_value=a[0][0]
max_value=a[0][0]

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] < min_value:
            min_value = a[i][j]

        if a[i][j] > max_value:
            max_value = a[i][j]

print(min_value)
print(max_value)
