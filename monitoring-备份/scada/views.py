from django.shortcuts import render
from django.http import JsonResponse
import pymssql

# Create your views here.

#实验函数
def realtime_views(request):
    return render(request,'form.html')

def zheng_views(request):
    return render(request,'zhengxing.html')

def zh2_views(request):
    return render(request,'gzhengxing.html')

def zxdata_views(request):
    # print(111)
    aList = {}
    bList = {}
    conn = pymssql.connect(host="192.168.13.240", user="sa", password="Admin123", database="DATA", charset="utf8")
    cursor = conn.cursor()

    sql = "select top 1 * from Table_3 order by id desc"
    try:
        cursor.execute(sql)

        result = cursor.fetchall()
        result = result[0]
        print(result)
        aList['sj'] = str(result[1])
        aList['b1'] = result[2]
        aList['b2'] = result[3]
        aList['b3'] = result[4]
        aList['b4'] = result[5]
        aList['lm1'] = result[6]
        aList['lm2'] = result[7]
        aList['lm3'] = result[8]
        aList['lm4'] = result[9]
        # print(aList)

        return JsonResponse(aList)
    except:
        bList['sj'] = '2018.11.8 10:22:55'
        bList['b1'] = 1
        bList['b2'] = 1
        bList['b3'] = 1
        bList['b4'] = 1
        bList['lm1'] = 1
        bList['lm2'] = 1
        bList['lm3'] = 1
        bList['lm4'] = 1
        print('链接错误')

        return JsonResponse(bList)



#ajax请求数据调用函数，用于响应数据
def ajax_views(request):
    print(22222)
    #创建数据库链接
    conn = pymssql.connect(host="192.168.13.240", user="sa", password="Admin123", database="DATA", charset="utf8")
    #创建游标
    cursor = conn.cursor()
    #创建两个空字典
    aList = {}
    bList = {}
    #编写sql查询语句，查询最新一条数据
    sql = 'select top 1 * from Table_4 order by id desc'
    #避免查询数据库时因异常而崩溃，在此捕获异常
    try:
        #执行sql查询操作
        cursor.execute(sql)
        #获取查询结果，格式为列表
        result = cursor.fetchall()
        #因为只有一条结果，不用循环，通过下标取出
        result = result[0]
        # print(result)
        #根据需求将不同数据按键值对形式放入字典中，用于返回数据
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
        aList['ssj'] = result[1][13:15]
        # print(aList)
        #拿到数据后，以json形式响应给前端
        return JsonResponse(aList)
    #若出现异常则返回假数据，为了用户体验
    except:
        bList['riqi'] = '2018/09/30'
        bList['sj'] = '10:45:30'
        bList['st1'] = '0'
        bList['st2'] = '0'
        bList['st3'] = '0'
        bList['a'] = '0'
        bList['b'] = '0'
        bList['c'] = '0'
        bList['x'] = '0'
        bList['y'] = '0'
        bList['z'] = '0'
        bList['jd1'] = '0'
        bList['jd2'] = '0'
        bList['jd3'] = '0'
        bList['jd4'] = '0'
        bList['jd5'] = '0'
        bList['jd6'] = '0'
        bList['l'] = ['0', '0', '0', '0', '0', '0']
        print('连接数据库出错！')

        return JsonResponse(bList)

#手机端访问时响应的页面
def shouji_views(request):

    # return render(request,'scada_yidong.html')
    #此处连接数据库查询，为了在用户首次访问时就能看到数据
    print(33333)
    conn = pymssql.connect(host="192.168.13.240", user="sa", password="Admin123", database="DATA", charset="utf8")
    cursor = conn.cursor()
    aList = {}
    bList = {}

    sql = 'select top 1 * from Table_4 order by id desc'

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        result = result[0]
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

        #if语句是判断现在机器运行状态，因目前没有数据，先注释掉
        # if result[8] == 1:
        #     aList['tz'] = 'red'
        #     aList['dd'] = 'gray'
        #     aList['yx'] = 'gray'
        # elif result[9] == 1:
        #     aList['tz'] = 'gray'
        #     aList['dd'] = 'yellow'
        #     aList['yx'] = 'gray'
        # elif result[10] == 1:
        #     aList['tz'] = 'gray'
        #     aList['dd'] = 'gray'
        #     aList['yx'] = 'green'

        #同时响应模板和模板所需要的数据
        return render(request, 'scada_yidong.html', aList)

    except:
        bList['riqi'] = '2018/09/30'
        bList['sj'] = '10:45:30'
        bList['st1'] = '0'
        bList['st2'] = '0'
        bList['st3'] = '0'
        bList['a'] = '0'
        bList['b'] = '0'
        bList['c'] = '0'
        bList['x'] = '0'
        bList['y'] = '0'
        bList['z'] = '0'
        bList['jd1'] = '0'
        bList['jd2'] = '0'
        bList['jd3'] = '0'
        bList['jd4'] = '0'
        bList['jd5'] = '0'
        bList['jd6'] = '0'
        bList['l'] = ['0', '0', '0', '0', '0', '0']
        print('连接数据库出错！')

        #出现异常时响应假数据
        return render(request, 'scada_yidong.html', bList)


#历史坐标数据折线图界面，刷新时调用此函数，返回json类型历史坐标数值
#直接查询历史数据时候调用此函数，用于响应模板
def history_views(request):
    # return render(request,'history.html')
    return render(request,'test.html')

#从首页跳转到历史坐标折线图调用此函数
def coordinates_views(request):
    #在此查询数据库目的为了让用户看到页面同时看到数据
    conn = pymssql.connect(host="192.168.13.240", user="sa", password="Admin123", database="DATA", charset="utf8")
    cursor = conn.cursor()
    aList = {}
    bList = {}
    aList['sj'] = []
    aList['a'] = []
    aList['b'] = []
    aList['c'] = []
    aList['x'] = []
    aList['y'] = []
    aList['z'] = []
    bList['sj'] = []
    bList['a'] = []
    bList['b'] = []
    bList['c'] = []
    bList['x'] = []
    bList['y'] = []
    bList['z'] = []

    sql = 'select top 100 * from Table_4 order by id desc'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            aList['sj'].append(int(i[1][13:15]))
            aList['a'].append(i[2])
            aList['b'].append(i[3])
            aList['c'].append(i[4])
            aList['x'].append(i[5])
            aList['y'].append(i[6])
            aList['z'].append(i[7])

        # result = result[0]
        # # print(result)
        # aList['riqi'] = result[1][:10]
        # aList['sj'] = result[1][10:]
        # aList['st1'] = result[8]
        # aList['st2'] = result[9]
        # aList['st3'] = result[10]
        # aList['a'] = result[2]
        # aList['b'] = result[3]
        # aList['c'] = result[4]
        # aList['x'] = result[5]
        # aList['y'] = result[6]
        # aList['z'] = result[7]
        # aList['jd1'] = result[11]
        # aList['jd2'] = result[12]
        # aList['jd3'] = result[13]
        # aList['jd4'] = result[14]
        # aList['jd5'] = result[15]
        # aList['jd6'] = result[16]
        # aList['l'] = [result[11], result[12], result[13], result[14], result[15], result[16]]
        # aList = aaa()
        # return JsonResponse(aList)

        #同时响应模板和模板所需要的数据
        return render(request,'test.html',aList)

    except:
        #出现异常时响应模拟数据
        bList['sj'].append(30)
        bList['a'].append('0')
        bList['b'].append('0')
        bList['c'].append('0')
        bList['x'].append('0')
        bList['y'].append('0')
        bList['z'].append('0')
        # bList['l'] = ['0', '0', '0', '0', '0', '0']
        print('连接数据库出错！')

        return JsonResponse(bList)

#历史坐标数据页面刷新时调用此函数，响应json类型数据
def query_views(request):
    conn = pymssql.connect(host="192.168.13.240", user="sa", password="Admin123", database="DATA", charset="utf8")
    cursor = conn.cursor()
    aList = {}
    bList = {}
    aList['sj'] = []
    aList['a'] = []
    aList['b'] = []
    aList['c'] = []
    aList['x'] = []
    aList['y'] = []
    aList['z'] = []
    bList['sj'] = []
    bList['a'] = []
    bList['b'] = []
    bList['c'] = []
    bList['x'] = []
    bList['y'] = []
    bList['z'] = []

    sql = 'select top 100 * from Table_4 order by id desc'
    try:
        #执行sql语句
        cursor.execute(sql)
        #获取执行结果，结果为列表，每条记录以元组形式存放与列表
        result = cursor.fetchall()

        #使用for循环，拿到每一条记录
        for i in result:
            aList['sj'].append(int(i[1][13:15]))
            aList['a'].append(i[2])
            aList['b'].append(i[3])
            aList['c'].append(i[4])
            aList['x'].append(i[5])
            aList['y'].append(i[6])
            aList['z'].append(i[7])
        #拿到所有结果后，以json形式响应到前端
        return JsonResponse(aList)

    except:
        #模拟数据，出现异常时响应，避免服务器崩溃
        # bList['riqi'] = '2018/09/30'
        bList['sj'] = [30,33,36,39,42]
        bList['a'] = [30,33,36,39,42]
        bList['b'] = [30,33,36,39,42]
        bList['c'] = [30,33,36,39,42]
        bList['x'] = [30,33,36,39,42]
        bList['y'] = [30,33,36,39,42]
        bList['z'] = [30,33,36,39,42]
        # bList['l'] = ['0', '0', '0', '0', '0', '0']
        print('连接数据库出错！')

        return JsonResponse(bList)

















