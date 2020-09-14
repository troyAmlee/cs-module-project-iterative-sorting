# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in arr[i:]:
            if(arr[smallest_index] > j):
                smallest_index = arr.index(j)

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr

a = [45, 37, 66, 89, 54, 81, 2, 1, 7]

print(f"Selection Sort: {selection_sort(a)}")

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    first_index = 0
    second_index = 0
    count = True
    counted = 0
    if(len(arr) == 0):
        return arr
    while(count == True):
        for i,j in enumerate(arr):
            if(i + 1 != len(arr)):
                first_index = i
                second_index = i + 1
                if(arr[second_index] < arr[first_index]):
                    temp = arr[first_index]
                    arr[i] = arr[second_index]
                    arr[second_index] = temp
                    counted = counted + 1
            elif(i == len(arr) - 1):
                if(counted > 0):
                    count = True
                    counted = 0
                else:
                    count = False
                    break
            else:
                break



    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(f"Bubble Sort: {bubble_sort(arr1)}")

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
