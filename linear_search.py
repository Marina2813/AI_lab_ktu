def search(arr,n):
    flag = 0
    for i in arr:
        if n == i:
            flag = 1 
            break
    if flag == 1:
        print("Element found")
    else:
        print("element not found!!!")

arr = list(map(int,input("Enter the array: ").split()))
n = int(input("Enter the element to be searched: "))
search(arr,n)