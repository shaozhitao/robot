import pymssql
from multiprocessing import Pool

pool = Pool(processes = 4)
conn = pymssql.connect(host="192.168.0.246", user="sa", password="Admin123", database="DATA", charset="utf8")

def create_cur():
    aList = {}
    # conn = pymssql.connect(host="192.168.0.246", user="sa", password="Admin123", database="DATA", charset="utf8")
    # cursor = conn.cursor()
    # sql = 'select top 1 * from Table_1 order by id desc'

    try:
        print(11111)
        aList = {}
        cursor = conn.cursor()
        sql = 'select top 1 * from Table_1 order by id desc'

        # result = r.get()
        # print(11111)
        cursor.execute(sql)
        # print(22222)
        result = cursor.fetchall()
        # print(33333)
        result = result[0]
        print(result)
        aList['riqi'] = result[1][:10]
        aList['sj'] = result[1][10:]
        aList['st1'] = result[8]
        aList['st2'] = result[9]
        aList['st3'] = result[10]
        aList['a'] = result[2]
        aList['b'] = result[3]
        aList['c'] = result[4]
        aList['x'] = result[5]
        aList['y'] = result[6]
        aList['z'] = result[7]
        aList['jd1'] = result[11]
        aList['jd2'] = result[12]
        aList['jd3'] = result[13]
        aList['jd4'] = result[14]
        aList['jd5'] = result[15]
        aList['jd6'] = result[16]
        aList['l'] = [result[11],result[12],result[13],result[14],result[15],result[16]]
        # cursor.close
        return aList
    except:
        print(11111)
        print('数据库链接错误data')

def aaa(conn):
    # sql = 'select top 1 * from Table_1 order by id desc'
    r = pool.apply_async(create_cur)
    # r = create_cur()
    r = r.get()
    return r