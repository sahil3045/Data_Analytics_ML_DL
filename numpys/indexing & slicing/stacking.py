'''
np.vstack() vertically stacking , row wise 
np.hstack() horizontally stacking, column wise 
'''

import numpy as np
arr1 = np.array([3, 4, 5, 6, 7, 8])
arr2 = np.array([1, 2, 3, 5, 5, 8])

print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))


'''
splitting
np.split() - split equally 
np.hsplit()
np.vsplit()
'''
print(np.split(arr1,2))