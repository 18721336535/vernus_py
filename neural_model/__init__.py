from array import array

import numpy as np

# a = np.arange(9).reshape((3, 3))
# # a = array([[0, 1, 2],
# #            [9, 4, 5],
# #            [6, 7, 8]])
# print(a)  # 全局最大
# print(np.max(a))  # 全局最大
#
# print(np.max(a, axis=0))  # 每列最大
#
# print(np.max(a, axis=1))  # 每行最大
#
# print("==",np.where(a==np.max(a)))
#
# b = np.where(a==np.max(a))
# print("=b=",b)
# print("=b=",b[0])
# print("=b=",b[0][0])



# print("--",np.where(a==np.max(a,axis=0)))
#
# print("-X-",np.where(a==np.max(a,axis=1)))
print(np.arange(3))
a= []
b= []
two_dim_matrix_one= []
two_dim_matrix_two= []

for i in np.arange(3):
    a.append(i+3)
    b.append(2*i)
two_dim_matrix_one.append(np.array(a))
two_dim_matrix_one.append(np.array(b))
a1= []
b1= []
c1= []
for i in np.arange(2):
    a1.append(i+1)
    b1.append(2+i)
    c1.append(3)

two_dim_matrix_two.append(np.array(a1))
two_dim_matrix_two.append(np.array(b1))
two_dim_matrix_two.append(np.array(c1))

r1=np.array(two_dim_matrix_one)
r2=np.array(two_dim_matrix_two)
print('r1: %s' %(r1))
print('r2: %s' %(r2))



two_multi_res = np.dot(r1, r2)

print('two_multi_res: %s' %(two_multi_res))

# # 2-D array: 2 x 3
# two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# # 2-D array: 3 x 2
# two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])
#
# two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
# print('two_multi_res: %s' %(two_multi_res))
#
# # 1-D array
# one_dim_vec_one = np.array([1, 2, 3])
# one_dim_vec_two = np.array([4, 5, 6])
# one_result_res = np.dot(one_dim_vec_one, one_dim_vec_two)
# print('one_result_res: %s' %(one_result_res))


