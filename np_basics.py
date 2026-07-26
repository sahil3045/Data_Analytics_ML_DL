import numpy as np 

temperatures = np.array([28.5, 33.7, 32.9, 31.6])
average = np.mean(temperatures)
print(average)
#print(np.min(temperatures))

#if you want to check the shape of an array 
#print(temperatures.shape)

#if you want to check the total no of elements of an array 
#print(temperatures.size)

#if you want to check the dimension of an array 
#print(temperatures.ndim)

#if you want to check the data type of an array 
#print(temperatures.dtype)

#if you want to change the data type of an array 
#print(temperatures.astype(int))

'''
#adv of numpys (numbers in python )
#used to calculate data from millions of numbers in mili seconds 
#1 speed 80 to 100 perc faster
#2 less memory 
#3 easy math operations 
'''

#one dimensional array 
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

#two dimensional array 
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(arr_2d)
print(arr_2d.ndim)

#default values array 
zeroes_array = np.zeros(3) # here 3 is the size/shape that you want of your array 

ones_arr = np.ones((2,3))
print(ones_arr)

#if you want custom value in place of zero or 1 
full_arr = np.full((3,3), 9)
print(full_arr)

#creating sequences of numbers in umpy 
#arange(start, stop, step )

arrr = np.arange(1, 10, 3)
print(arrr)

#if you want to create identity matrix 
im = np.eye(4)
print(im)

#math operators 
print(temperatures + 2)
print(temperatures * 2)
print(temperatures ** 2)


#aggregation function 
'''
np.sum(array) adds all
np.mean(array) avg 
np.min(array) minimum element
np.max(array) maximum element 
np.std(array) standard deviation 
np.var(array) variance 
'''