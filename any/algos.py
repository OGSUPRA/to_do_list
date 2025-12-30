
def binarySearch (list,element):
    start_list = 0
    last_list = len(list) - 1
    while start_list <= last_list:
        middle_index = (start_list + last_list) // 2
        if list[middle_index] < element:
            start_list = middle_index + 1
        elif list[middle_index] > element:
            last_list = middle_index - 1
        else:
            return middle_index
        
    return None

def searchSmallest (list):
    smallest = list[0]
    index_smallest = 0
    for i in range (1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            index_smallest = i
    return index_smallest

def selectionSort (list):
    new_list = []
    copy_list = list.copy()
    for i in range (len(copy_list)):
        smallest = searchSmallest(copy_list)
        new_list.append(copy_list.pop(smallest))
    return new_list

def sum_list(list):  
    sum_items = 0
    for i in list:
        sum_items += i
    return sum_items

def sum_list_rec (list):
    if list == []:
        return 0
    return list[0] + sum_list_rec(list[1:])

def count_elements (list):
    if list == []:
        return 0
    return 1 + count_elements(list[1:])

def max_search(list):
    max_element = list[0]
    max_element_index = 0
    for i in range (1, len(list)):
        if list[i] > max_element:
            max_element = list[i]
            max_element_index = i
    return max_element_index

def max_search_rec(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list [1]
    max_search_rec_rec = max_search_rec(list[1:])
    return list[0] if list[0] > max_search_rec_rec else max_search_rec_rec

def quickSort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i < pivot]
        greater = [i for i in list[1:] if i > pivot]
        return (quickSort(less) + [pivot] + quickSort(greater))



