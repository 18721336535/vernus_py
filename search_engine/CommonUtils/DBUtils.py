import logging
import traceback

import pymysql


class DBUtils:
    def __init__(self):
        print('')

    def condb(self):
        db = pymysql.connect(
            "localhost",
            "root",
            "123456",
            "zbqdb",
            3306)
        return db


    def selSql(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.condb().cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        print("Database version : %s " % data)

        # 关闭数据库连接
        self.condb().close()


    def selectSql(self):
        db = self.condb()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT * from zbqinfotb limit 10")
        # 使用 fetchone() 方法获取单条数据.
        results = cursor.fetchall()
        list = []  ## 空列表
        dct = {}
        for row in results:
            listRow = []
            name = row[0]
            type = row[1]
            engine = row[2]
            listRow.append(name)
            listRow.append(type)
            listRow.append(engine)
            list.append(listRow)
            dct.update({name: listRow})
            print(dct[name])

        print(list)
        for i in dct.keys():
            print(i)
            print(dct[i])
        # 关闭数据库连接
        db.close()


    def insertSql(self,id, name, book):
        # SQL 插入语句
        db = self.condb()
        cursor = db.cursor()
        print("begin insert ")
        sql = "INSERT INTO zbqinfotb(id,name, book) VALUES (\'" + id + "\', \'" + name + "\', \'" + book + "\')"
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except BaseException as e:
            # Rollback in case there is any error
            db.rollback()
            print("roll back ")
            msg = traceback.format_exc()
            print(msg)
            logging.exception(e)
        db.close()


    # if __name__ == '__main__':
    #     selectSql()
    #     insertSql("a2", "tensorFlow", "tensorFlow book")
