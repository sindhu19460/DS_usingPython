def bubble_sort(array):
    for i in range(0,len(array)-1):
        for j in range(0,len(array)-1):

            if(array[j]>array[j+1]):

                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    return array


lst = []
array_size = int(input("Enter the size of the array="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)
    
print("After sorting\n",bubble_sort(lst))


