def find_minimum_value(values):
    special_value = values[0]
    for value in values:
        if(value< special_value):
            special_value = value
    return special_value



def insertion_sort(values):
    smallest_list=[]
    while(len(values)>0):
        smallest = find_minimum_value(values)
        values.remove(smallest)
        smallest_list.append(smallest)
    return smallest_list
    #[all numbers jumbled (1,2,3,6) take them out as they get moved to new lists]
    #[1]
    #[1,2]
    #[1,2,3]
    #[1,2,3,6]
unsorted = [5,7,3,6,2,7,3,4]
sorted = insertion_sort(unsorted)
print(sorted)

