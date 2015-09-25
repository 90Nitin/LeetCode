__author__ = 'nsrivas3'

# TTD
# 1. A function to shift 1 element to the right in a given array
# 2. Call the function k times to shift all the required elements in the array


arr = [1,2,3,4,5,6,7,8]

def Rotate1(arr):
    len = arr.__len__()
    temp = arr[0]
    temp2 = arr[len-1]
    for i in range(1,len):
        temp1 = arr[i]
        arr[i] = temp
        temp = temp1
        print("I" + str(i)+str(temp))
    arr[0] = temp2
    return(arr)

a = Rotate1(Rotate1(Rotate1(arr)))