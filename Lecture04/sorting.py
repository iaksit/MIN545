

a = [ 1, 2 , -4, 7, 8, 3, 15 ]

def swap(arr, i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(arr):
    for j in range(len(arr)):
        smallest = 100000000
        smallest_place = -1
        for i in range(j,len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_place = i
        swap(arr, j, smallest_place)

def bubble_sort(arr):
    is_change = True
    top = len(arr)
    while is_change:
        is_change = False
        for j in range(1,top):
            if arr[j-1] > arr[j]:
                swap(arr, j-1, j)
                is_change = True
        top = top - 1
    
    
