import cmath

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




