#Binary search only works for a sorted list , so we import
#insertion sort function already made 

def binary_search(arr,target):
    
    l=0
    r=len(arr)-1
    
    while l<=r:
        m=(l+r)//2
        if arr[m]>target:
            r=m-1
        elif arr[m]<target:
            l=m+1
        else:
            return m
    return -1

if __name__=='main':
    x=list(map(int,input().split()))
    y=int(input())
    print(f"{binary_search(x,y)}th index.")
    