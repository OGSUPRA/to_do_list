list = [1,4,4,6,9,3]
target = 8
def twoSum(list,target):
    list_2 = []
    for i in list:
        if i < target:
            list_2.append(i)
    for i in list_2:
        print("i =",i)
        for g in list_2[list_2.index(i)+1:]:
            print("g =",g)
            if (i + g) == target:               
                return [list_2.index(i), list_2.index(g)] 

def binary_search(list,element):
    start_list = 0
    last_list = len(list) - 1
    while  

print(twoSum(list,target))
print