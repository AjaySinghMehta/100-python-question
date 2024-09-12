'''
we are given an array we need to reverse it 
ex = array =  [1,2,3,4] ,  result = [4,3,2,1] 

there are many ways to do this i will do it in two ways
first one is for python only 

'''

# method 1 

arr = list(map(int, input('enter array : ').split()))
result = arr[::-1]
print('first method output (using array[::-1]): ',result)


# second method :
for i in range(len(arr)//2):
    arr[i] = arr[i]+arr[len(arr)-1]
    arr[len(arr)-1] = arr[i] -  arr[len(arr)-1]
    arr[i] = arr[i] -  arr[len(arr)-1]
    
print('using second method where we swap compliment elements : ',arr)
    
