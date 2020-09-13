n,k = map(int,input().split())
arr_list = [int(x) for x in input().split()]
    
def bsearch(arr,l,r,a):
    if r >= l:
        mid = (r+l)//2
        if arr[mid] == a:
            print('yes')
        elif arr[mid] > a:
            bsearch(arr,l,mid-1,a)
        else:
            bsearch(arr,mid+1,r,a)
    else:
        print('no')
            
bsearch(arr_list,0,len(arr_list)-1,k)
