
from CommonUtils.DBUtils import *

class Step1_WsetGenerate:
    wset = []

    def __init__(self, wset):
        self.wset = wset

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

        for str in data:
            self.wset.append(str)

        print(self.wset)


wset = []
test = Step1_WsetGenerate(wset)
test.build_wset()
