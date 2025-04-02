def freq(lst):
    cou = {}
    for i in lst:
        cou[i] = cou.get(i, 0) + 1
    return cou

lst = [1,5,7,9,6,4,2,3,4,8,4,6,3,4,9,2,8,5,4]
print(freq(lst))
