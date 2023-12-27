def selection_sortdesc(array):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:

                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array

lst = []
array_size = int(input("Enter the size of the array="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)
    
print("Desc sorting\n",selection_sortdesc(lst))
