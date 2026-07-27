import numpy as np 

#indexing is selecting a specific element from an array 
arr = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
print(arr[0])
print(arr[-1])




#slicing 
#array[start:stop:step]
#start - exact index
#stop - index+1
print(arr[1:5])
print(arr[1:5:2])
print(arr[: : -1]) #if you want to print in reverse 

#fancy indexing  - selecting multiple elements at once
print(arr[[0, 3, 5]]) #--use double brackets 


#filtering data / Boolean masking
print(arr[arr>25])


#reshaping - use to convert 1d array to 2d array
reshaped_arr = arr.reshape(3,3)
print(reshaped_arr)

#flattening array - used to convert multi dimensional array into 1d array 
#.ravel() - views 
#.flatten() - copy 
arr_2d = np.array([[1, 2, 3,], [3, 4, 5]])
print(arr_2d.ravel())
print(arr_2d.flatten())


'''
np.insert(array, index, value, asix="none")
axis = 0 - row wise insert
axis = 1 - column wise insert 
'''

new_arr = np.insert(arr, 3, 75)
print(new_arr)

new2_arr = np.insert(arr_2d,1, [5, 6], axis=None)
print(new2_arr)

arr_new = np.append(arr, [30,35])

#concatenate
#np.concatenate((arr1, arr2), axis=None)
#asix 0 - row wise
#axis 1 - columnwise 

#remove elements of array 
#np.delete(array, index, axis = None)
#new_arr = np.delete(arr, 0)
#print(new_arr)

# for 2d arr
#new_arr_2d = np.delete(arr_2d, 0,axis=0)

