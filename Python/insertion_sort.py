def insertion_sort(arr):
    
    for i in range(1,len(arr)): #outer loop representing the pointer (i)
        
        j=i#seperate pointer to check elements before (i)
        
        while arr[j-1] > arr[j] and j>0:#this runs untill all the elements before (i) are sorted
            
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j -= 1
            
if __name__=='__main__':            
    x=list(map(int,input().split()))
    insertion_sort(x)
    print(x)