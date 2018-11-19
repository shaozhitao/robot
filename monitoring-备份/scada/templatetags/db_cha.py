from django import template
import pymssql
from django.utils.safestring import mark_safe

# conn = pymssql.connect(host="192.168.0.246", user="sa", password="Admin123", database="DATA", charset="utf8")
# cursor = conn.cursor()
#
# register = template.Library()
#
# @register.simple_tag
# def worker(sql):
#     try:
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         return result
#     except:
#         print('进程池内对数据库查询')
