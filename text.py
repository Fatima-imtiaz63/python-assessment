import numpy as np

arr1 = np.array([10, 13, 25, 78, 76, 98])
print("1d Array:", arr1)
arr2 = np.array([[34, 45, 65],
                 [90, 89, 78],
                 [45, 56, 67]])
print("2d Array:", arr2)
print("shape of arr1:" , arr1.shape)
print("shape of arr2:" , arr2.shape)
print("sum of arr1:" , np.sum(arr1))
print("Max of arr1:" ,np.max(arr1))
print("min of arr1:", np.min(arr1))
print("arr1 * 5:", arr1 * 5)
print("arr2 +2:", arr2 + 2)