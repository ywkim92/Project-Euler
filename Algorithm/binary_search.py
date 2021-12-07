def binary_search_recursion(arr, n):
    if not arr: return False
    elif len(arr)==1:
        if arr[0]==n: return True
        else: return False
    else:
        first = 0
        last = len(arr)
        mid = (first+last)//2
        if arr[mid]==n: return True
        elif arr[mid]>n: return binary_search_recursion(arr[first:mid], n, )
        else: return binary_search_recursion(arr[mid+1:last], n, )
        
def binary_search(array, n):
    found = False
    first = 0
    last = len(array) - 1
    while first<=last and not found:
        mid = (first+last)//2
        if array[mid]==n: found= True
        elif array[mid]>n: last= mid - 1
        else: first = mid + 1
    return found
