import pymysql

# db= pymysql.connect("localhost","root",
#                     "123456","zbqdb",3306)

def condb():
    db= pymysql.connect("localhost","root",
                        "123456","zbqdb",3306)
    return db

def selSql():

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = condb().cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print ("Database version : %s " % data)

    # 关闭数据库连接
    condb().close()

def selectSql():
    db = condb()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * from zbqinfotb limit 10")

    # 使用 fetchone() 方法获取单条数据.
    results = cursor.fetchall()

    for row in results:
        name = row[0]
        type = row[1]
        engine = row[2]
        print(name, type, engine)

    # 关闭数据库连接
    db.close()

selectSql()