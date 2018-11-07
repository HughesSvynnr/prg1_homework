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



def find_position(values,element):
    index=0
    for value in values:
        if(value == element):
            return index
        index += 1



def selection_sort(values):
    count = 0
    while(count < len(values)):
        smallest_value = find_minimum_value(values[count:])
        position = find_position(values,smallest_value)
        values[position]=values[count]
        values[count]= smallest_value
        count += 1
    return values

unsorted = [2,3,4,5,32,4,54]
print(selection_sort(unsorted))