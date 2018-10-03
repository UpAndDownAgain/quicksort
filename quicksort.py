from random import randint

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[randint(0,len(array)-1)]
        less = [i for i in array if i < pivot]
        equal = [i for i in array if i == pivot]
        more = [i for i in array if i > pivot]
        return quicksort(less) + equal + quicksort(more)

arr = [1,4,56,4,8,5,6,74,1,23,3,54]
print(quicksort(arr))