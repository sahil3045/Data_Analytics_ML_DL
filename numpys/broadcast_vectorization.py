import numpy as np
'''
this is using basic loops uses more time 

prices = [100, 200, 250, 300]
discount = 10
final_prices= []
for i in prices:
    final_price = i - (i * discount/100)
    final_prices.append(final_price)
    
print(final_prices)

'''

#using broadcasting

prices = np.array([100, 200, 250, 300])
discount = 10 
final_prices = (prices - prices*discount/100) 
print(final_prices)

'''
#how numpy handles arrays of differnet shapes
#1 matching dimensions for eg [1,2,3] + [1, 2, 3] = [1, 4, 6]
2 expanding single elements for eg [1,2,3] + 10 = [11, 12, 13]
3 incompatible shapes for wg [1, 2, 3] + [2, 3] = error

'''

#now broadcasting for 1d to 2d array 
matrix  = np.array([[1,2,3], [2,3,4]])
vector = np.array([10, 10, 10])
err = np.array([1, 2])
#now when we add this err in our 2d array it will give error because its shape is different 

result = matrix + vector 



# Vectorization 
arr1 = np.array([1,2,3])
arr2 = np.array([2,3,4])
multi = arr1 * 2
res = arr1 + arr2
print(res)

