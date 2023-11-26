#program to print the largest number in an array
def largest_num(arr):
    largest = arr[0]
    for i in arr:
        if largest<i:
            largest=i
    return largest

arr = list(map(int,input("Enter your array: ").split()))
largest = largest_num(arr)
print(f"The largest number in the list is: {largest} ")