def greater(a,b):
    if(a>b):
        return True 
    else:
        return False
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if(greater(arr[j],arr[j+1])):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr 
def main():
    print("Enter the Array Elements:")
    arr=list(map(int,input().split()))
    print("*** Sorted Array By using the Bubble Sort***")
    print(bubble_sort(arr))
if __name__=="__main__":
    main()
