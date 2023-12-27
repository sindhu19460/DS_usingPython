def partition(array,low,high):

    pivot = array[high]
    i = low -1

    for j in range(low,high):
        if (array[j] <= pivot):
            
            i+=1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    temp = array[i+1]
    array[i+1] = array[high]
    array[high] = temp
    return i+1

def quick_sort(array,low,high):

    if(low < high):

        pi = partition(array,low,high)

        quick_sort(array,pi+1,high)
        quick_sort(array,low,pi-1)


lst = []
array_size = int(input("Enter the size of the array="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)

low = 0
high = len(lst)-1
    
quick_sort(lst,low,high)
print("Quick sorting\n",lst)
