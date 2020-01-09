def heapify(array,i,n):
    maximum = i
    l = 2*i +1
    r = 2*i +2
    
    if r < n:
        if array[r] > array[i] and array[r] > array[l]:
            maximum = r
    
    if l < n:
        if array[l] > array[maximum]:
            maximum = l
    if maximum != i:
        array[i],array[maximum] = array[maximum],array[i]
        heapify(array,maximum,n)

def heapsort(array):
    n = len(array)
    for i in range(int((n/2)-1),-1,-1):
        heapify(array,i,n)

    for i in range(n-1,0,-1):
        print(i)
        array[i],array[0] = array[0],array[i]
        heapify(array,0,i)

        

array = [1,9,87,93,4,6,8,9,2,45,8]
heapsort(array)
print(array)
