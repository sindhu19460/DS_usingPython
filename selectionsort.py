def selection_sort(array):

    for i in range(0, len(array)-1):
        index = i

        for j in range(i+1, len(array)):

            if array[j] < array[index]:
                index = j

        temp = array[index]
        array[index] = array[i]
        array[i] = temp

    return array


lst = []
array_size = int(input("Enter the size of the array="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)
    
print("After sorting\n",selection_sort(lst))

