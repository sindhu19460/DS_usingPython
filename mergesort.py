def mergeSort(array):

    if (len(array)>1):
        mid = len(array)//2
        left = array[:mid] 
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)


        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i] <= right[j]:

                array[k] = left[i]

                i+=1

            else:
                array[k] = right[j]
                j+=1

            k+=1


        while i<len(left):
            array[k] = right[i]
            j += 1
            k += 1


lst = []
array_size = int(input("Enter the size of the array="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)

mergeSort(lst)
print(lst)
