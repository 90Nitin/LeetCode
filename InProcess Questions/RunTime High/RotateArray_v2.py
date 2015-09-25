__author__ = 'nsrivas3'

def rotate1(arr,len):
    temp = arr[0]
    temp2 = arr[len-1]
    for i in range(1,len):
        temp1 = arr[i]
        arr[i] = temp
        temp = temp1
        print("I" + str(i)+str(temp))
    arr[0] = temp2
    return(arr)

def rotate(arr, k):
    len = arr.__len__()
    counter = 0
    while counter<k:
        arr = rotate1(arr,len = len)
        counter = counter + 1

arr = [1,2,3,4,5,6,7,8,9,0,0]

rotate(arr,3)