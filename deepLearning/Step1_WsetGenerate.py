import re

from CommonUtils.DBUtils import *


class Step1_WsetGenerate:
    wset = set()
    sorted_wset = set()
    sorted_char_set = set()
    totalset = set()

    def build_wset(self):
        cloum_names = ['brand', 'series', 'engine', 'displacement', 'transmission', 'pyear', 'sell_name']
        for cln in cloum_names:
            self.select_by_cloum(cln)

    def select_by_cloum(self, cloum):

        sql = "select  " + cloum + " from Car_Model_Info"
        db = DBUtils.condb(self)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            self.wset.add(row[0])


    def splite_word(self, wset):
        print(','.join(wset))
        temp_wset = set()
        # str = ','.join(wset)
        # 多模式匹配
        # it = re.finditer(r"[\u4e00-\u9fa5]+|[A-Za-z0-9|.]+", str)
        # for match in it:
        #     self.sorted_wset.add(match.group())
        # print('sorted_wset', self.sorted_wset)

        # ptt= re.compile(r"[\u4e00-\u9fa5]+|[A-Za-z0-9|.]+")
        ptt1= re.compile(r"[\u4e00-\u9fa5]+")
        ptt2= re.compile(r"[A-Za-z0-9|.]+")
        temp_set1 = ptt1.findall(','.join(wset))
        temp_set2 = ptt2.findall(','.join(wset))
        print('temp_set1',temp_set1)
        print('temp_set2',temp_set2)
        self.sorted_wset = set(sorted(temp_wset.union(temp_set1,temp_set2)))
        print(self.sorted_wset)


    def generate_charset(self,wset):
        charset = set(list(''.join(wset)))
        self.sorted_char_set = sorted(charset)
        for i in charset:
            print(i)
        print('sorted_char_set',self.sorted_char_set)


    def insert_word_char_set(self):
        self.totalset = set(sorted(self.sorted_wset.union(self.sorted_char_set)))
        self.totalset.remove(' ')
        print("self.totalset ",self.totalset)
        sql = "insert into  Wset_Weight(facture_name,wscore)values(%s,%s)"
        conn = DBUtils.condb(self)
        cursor = conn.cursor()
        for name in self.totalset:
            weight = 1.0;
            if len(name) > 1:
                weight = 10.0
            cursor.execute(sql,(name,weight))
            print("insert ",name)
            conn.commit()

# obj = Step1_WsetGenerate()
# obj.build_wset()
# obj.splite_word(obj.wset)
# obj.generate_charset(obj.wset)
# obj.insert_word_char_set()
