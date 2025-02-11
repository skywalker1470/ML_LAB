import numpy as np 
#calculating mean
M2113_arr = np.random.randint(0,100,35)
M2113_sum = 0 
for num in M2113_arr:
    M2113_sum+=num
mean = M2113_sum / len(M2113_arr)
print(f"The array is :{M2113_arr}")
print(f"The mean is : {mean}")
#calculating median
#M2113_arr = np.random.randint(1,100,20)
M2113_arr.sort()
print(f"The sorted array is : {M2113_arr}")
M2113_median_idx = -1
median = -1
if(len(M2113_arr)%2!=0):
    M2113_median_idx = len(M2113_arr) // 2
    median = M2113_arr[M2113_median_idx]
else:
    M2113_median_idx = len(M2113_arr) // 2
    median = (M2113_arr[M2113_median_idx] + M2113_arr[M2113_median_idx-1]) // 2 
print(f"The median is {median}")
 # calculating mode 
M2113_count = [0] * 100
mode = 0 
for i in range(len(M2113_arr)):
    temp = M2113_arr[i]
    M2113_count[temp] += 1
for i in range(len(M2113_count)):
    if(M2113_count[mode]<M2113_count[i]):
        mode = i
print(f"The array is : {M2113_arr}")
print(f"The mode is : {mode}")