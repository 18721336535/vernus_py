import numpy as np


from CommonUtils.DBUtils import DBUtils
from Step4_score_algorithm import Score_Algorithm
class Match_Entry:
    #idj t1
    def enty(self):
        #query mx
        sql = 'select id, ly_fv from  ly_fv_matrix'
        sql2 = 'select id, zs_fv from  zs_fv_matrix'
        conn = DBUtils().condb(self)
        coursor = conn.cursor()
        coursor.execute(sql)
        data = coursor.fetchall()

        coursor1 = conn.cursor()
        coursor1.execute(sql)
        data1 = coursor1.fetchall()
        for row in data:
            id = row[0]
            fv = row[1]
            fv_f_lst = self.strlst_to_num_lst(fv)
            zs_lst = []
            for row in data1:
                zs_lst.add(self.strlst_to_num_lst(row[1]))
            zs_num_lst = np.matrix(zs_lst)

        two_multi_res = np.dot(fv_f_lst, zs_lst)
        np.max(two_multi_res[0])

        # Score_Algorithm().match_function(fv_f_lst,zs_num_lst)

    def strlst_to_num_lst(self,lst):
        fv_lst = lst.split(',')
        fv_f_lst = []
        for f in len(fv_lst):
            fv_f_lst[f] = float(fv_lst[f])
        return fv_f_lst