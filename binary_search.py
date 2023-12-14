def binary_search(arr,n):
    arr_ = sorted(arr)
    print(arr_)
    low,high = 0,len(arr)-1
    while low <= high:
        mid = (low+high)//2
        mid_element = arr[mid]

        if mid_element==n:
            print(f"element {n} found at {mid}")



arr = list(map(int,input("Enter the array: ").split()))
n = int(input("Enter the number to be searched: "))

binary_search(arr,n)