def greater(a,b):
    if(a>b):
        return True 
    else:
        return False 
def Insertion_Sort(Arr):
    size=len(Arr)
    for i in range(1,size):
        temp=Arr[i]
        j=i 
        while j>0 and greater(Arr[j-1],temp):
            Arr[j]=Arr[j-1]
            j -=1 
        Arr[j]=temp 
    return Arr 
def main():
    print("Enter the Elements of Array: ")
    Arr=list(map(int,input().split()))
    print("*** Sorted Array By Using the Insertion Sort ***")
    print(Insertion_Sort(Arr))
if __name__=="__main__":
    main()


