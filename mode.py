import numpy as np 
arr = np.random.randint(1, 10 , 20)
#most repeated
count = [0] * 10
mode = 0 
for i in range(len(arr)):
    temp = arr[i]
    count[temp] += 1
for i in range(len(count)):
    if(count[mode]<count[i]):
        mode = i
print(f"The array is : {arr}")
print(f"The mode is : {mode}")