def merge(dict1,dict2):
    for i in dict2.keys():
       if i in dict1:
           dict1[i]=[dict1[i],dict2[i]]
       else:
            dict1[i]=dict2[i]
    return dict1

dict1={"name":"Nani","age":23,"location":"kadapa"}
dict2={"name":"Bujji","regno":63,"location":"tirupati"}
print(merge(dict1,dict2))
