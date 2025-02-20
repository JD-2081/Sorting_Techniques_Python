def greater(a,b):
    if(a>b):
        return True 
    else:
        return False 
def Bubble_Sort(arr):
    n=len(arr)
    swap=1
    for i in range(n-1):
        swap=0
        for j in range(n-i-1):
            if(greater(arr[j],arr[j+1])):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=1 
        if(swap==0):
            break 
    return arr 
def main():
    print("Enter the Elements of Array:")
    arr=list(map(int,input().split()))
    print("*** Sorted Array by Using the Bubble Sort ***")
    print(Bubble_Sort(arr))
if __name__=="__main__":
    main()