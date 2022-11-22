import random

def quicksort(arr, low , high):
    if(low < high):
        pi = partitionrand(arr, low, high)
        quicksort(arr , low , pi-1)
        quicksort(arr, pi + 1, high)
  
def partitionrand(arr , low, high):
    randpivot = random.randrange(low, high)
    arr[low], arr[randpivot] = arr[randpivot], arr[low]
    return partition(arr, low, high)
  
def partition(arr,low,high):
    pivot = high 
    i = low - 1 

    for j in range(low , high):
        if arr[j] <= arr[pivot]:
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)
  

n = int(input())
arr = []
for i in range(n):
    ele = int(input())
    arr.append(ele)

quicksort(arr, 0, len(arr)-1)
print(arr)
