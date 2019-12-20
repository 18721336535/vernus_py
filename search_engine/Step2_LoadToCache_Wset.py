
from CommonUtils.DBUtils import *
from CommonUtils.RedisUtils import *

class Step2_LoadToCache_Wset:

    dct_name_id = {}
    dct_name_score = {}
    def load_wset_to_cache(self):
        robj =    RedisUtils()
        robj.conRdb().delete('dct_name_id')
        robj.conRdb().delete('dct_name_score')
        print("dct_name_id",robj.getRDict("dct_name_id"))
        sql = 'select id,facture_name,wscore from Wset_Weight'
        conn = DBUtils().condb(self)
        coursor = conn.cursor()
        coursor.execute(sql)
        data = coursor.fetchall()
        for row in data:
            id = row[0]
            name = row[1]
            score = row[2]
            self.dct_name_id.__setitem__(name,id)
            self.dct_name_score.__setitem__(name,score)

        robj.setRDict("dct_name_id",self.dct_name_id)
        robj.setRDict("dct_name_score",self.dct_name_score)
        print("dct_name_id",robj.getRDict("dct_name_id"))


obj = Step2_LoadToCache_Wset()
obj.load_wset_to_cache()