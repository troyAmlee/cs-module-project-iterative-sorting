def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    # find the midpoint element
    # length//2
    while(left <= right):
        midpoint = (right + left) // 2
        if(arr[midpoint] == target):
            return midpoint
        elif(arr[midpoint] > target):
            right = midpoint - 1
        elif(arr[midpoint] < target):
            left = midpoint + 1
    return -1

a = [3, 4, 6, 16, 26, 28, 55, 56]

print(binary_search(a, 55))
print("-------")
print(binary_search(a, 100))



    
