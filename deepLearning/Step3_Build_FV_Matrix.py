import re

from CommonUtils.DBUtils import DBUtils
from CommonUtils.RedisUtils import RedisUtils


class Step3_Build_FV_Matrix:

    fv_size = 2 * 100

    def select_by_cloum(self):
        robj = RedisUtils()
        dct_name_id = robj.getRDict("dct_name_id")
        dct_name_score = robj.getRDict("dct_name_score")

        sql = "select id, brand, series, engine, displacement, transmission, pyear, sell_name from Car_Model_Info"
        db = DBUtils.condb(self)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            wset = set()
            id = row[0]
            wset.add(row[1])
            wset.add(row[2])
            wset.add(row[3])
            wset.add(row[4])
            wset.add(row[5])
            wset.add(row[6])
            wset.add(row[7])
            totalset = self.splite_word(wset).union(self.generate_charset(wset))
            totalset.remove(' ')
            print('totalset---', totalset)
            lst = [0] * self.fv_size
            for i in totalset:
                index = int(dct_name_id[i])
                lst[index] = dct_name_score[i]
            sql = "insert into  ly_fv_matrix(ly_id,ly_fv,ly_fv_wset)values(%s,%s,%s)"
            conn = DBUtils.condb(self)
            cursor = conn.cursor()

            str1 = ""
            for i in lst:
                str1 += ","+str(i)
            tempstr  = str1[1:len(str1)]

            print(tempstr)

            cursor.execute(sql,(str(id),str1,",".join(totalset)))
            conn.commit()


    def splite_word(self, wset):
        # print(','.join(wset))
        temp_wset = set()

        ptt1 = re.compile(r"[\u4e00-\u9fa5]+")
        ptt2 = re.compile(r"[A-Za-z0-9|.]+")

        temp_set1 = ptt1.findall(','.join(wset))
        temp_set2 = ptt2.findall(','.join(wset))
        # print('temp_set1',temp_set1)
        # print('temp_set2',temp_set2)
        return set(sorted(temp_wset.union(temp_set1, temp_set2)))

    def generate_charset(self, wset):
        charset = set(list(''.join(wset)))
        sorted_char_set = set(sorted(charset))
        return sorted_char_set


obj = Step3_Build_FV_Matrix()
obj.select_by_cloum()
