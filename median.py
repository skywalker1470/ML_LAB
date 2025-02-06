import numpy as np
arr = np.random.randint(1,100,20)
arr.sort()
print(f"The sorted array is : {arr}")
median_idx = -1
median = -1
if(len(arr)%2!=0):
    median_idx = len(arr) // 2
    median = arr[median_idx]
else:
    median_idx = len(arr) // 2
    median = (arr[median_idx] + arr[median_idx-1]) // 2 
print(f"The median is {median}")
