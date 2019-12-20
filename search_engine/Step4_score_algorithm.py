import cmath

import numpy as np


class Score_Algorithm:

    def match_function(self,fv1,fv2):

        molecule = float(0)
        for i in len(fv1):
            molecule += float(fv1[i])* float(fv2[i])

        temp1 = float(0)
        temp2 = float(0)
        for i in len(fv1):
            temp1 += float(fv1[i])*float(fv1[i])
            temp2 += float(fv2[i])*float(fv2[i])
        denominator1 = cmath.sqrt(temp1)
        denominator2 = cmath.sqrt(temp2)

        score = molecule/float(denominator1 * denominator2)

        return score

    def matrix(self,a,b):
        for i in np.arange(3):
            a[i] = i*i
            b[i] = 2*i
        c = list(a,b)


        two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
        # 2-D array: 3 x 2
        two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])

        two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
        print('two_multi_res: %s' %(two_multi_res))




