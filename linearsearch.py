
def linearsearch(array,key,n):
    for i in range(0,n):
        if (array[i] == key):
            return i
    return -1
    
#input
lst = []
array_size = int(input("Enter the number of elements="))

for i in range(0,array_size):
    ele = int(input("Enter the array elements="))
    lst.append(ele)
print(lst)


key_element_search = int(input("KeyElementSearch="))
length = len(lst)

result = linearsearch(lst,key_element_search,length)


if( result == -1 ):
    print("Not found")
else:
    print("Found ",result)