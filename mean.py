import numpy as np 
arr = np.random.randint(0,100,35)
sum = 0 
for num in arr:
    sum+=num
mean = sum / len(arr)
print(f"The array is :{arr}")
print(f"The mean is : {mean}")