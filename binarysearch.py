def binary_search(array,key):
    low = 0
    high = len(array)-1
    mid = 0

    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if array[mid] < key:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif array[mid] > key:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1


   
    
#input
lst = []
array_size = int(input("Enter the number of elements="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)
print(lst)


key_element_search = int(input("KeyElementSearch="))

result = binary_search(lst,key_element_search)

if(result == -1):
    print("Element is present at index",str(result))
else:
    print("Element is not present in array")