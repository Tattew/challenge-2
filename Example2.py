def printArr(arr, arr_size, sum):
     
    hashmap = {}
     
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in hashmap):
            print (f'sum {sum} is ({temp} + {arr[i]}) at indexes ({hashmap[temp]},{i})')
        hashmap[arr[i]] = i
 
# driver code
A = [3,2,4]
n = 6
printArr(A, len(A), n)