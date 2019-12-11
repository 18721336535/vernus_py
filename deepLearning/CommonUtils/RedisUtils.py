import redis

class RedisUtils:

    def conRdb(self):
        pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='123456',decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        return r


    def setRDict(self,name,dct):
        r = self.conRdb()
        r.hmset(name,dct)
        r.expire(name,3600*24*7)

    def getRDict(self,name):
        r = self.conRdb()
        return r.hgetall(name)



    # if  __name__=='__main__':
    #     rdb = conRdb()
    #     rdb.set('python_1','hello python')
    #     str = rdb.get("python_1")
    #     dct = {'a1':'1x','a2':'12x'}
    #     setRDict("dct1",dct)
    #     print(getRDict("dct1"))
    #     dcttemp = getRDict("dct1")
    #     list = dcttemp.keys()
    #     print(list)
    #     for key in list:
    #         print(key)
    #         value = dcttemp.get(key)
    #         print(key,value,sep = "=")




