import numpy as np
#np.isnan(array)
arr = np.array([10, 20, np.nan, 30, np.nan, 50])
print(np.isnan(arr))

#now to replace the nan value to num 
#np.nan_to_num(array, nan=value)
a = np.nan_to_num(arr,nan = 15)
print(a)

#infinite 
#np.isinf(array)

arr1 = np.array([10, 20, np.inf, 30, -np.inf, 50])
print(np.isinf(arr1))
clean = np.nan_to_num(arr1, posinf = 1000, neginf=-1000)
print(clean)
