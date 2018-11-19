from django.conf.urls import url
from .views import *

#scada　app　的路由，功能根据不同请求做对应响应
urlpatterns = [
    url(r'^realtime/',realtime_views),
    url(r'^a1/',ajax_views),
    url(r"^zh/",zheng_views),
    url(r"^zh2/",zh2_views),
    url(r'^zxdata/',zxdata_views),
    url(r'^data/',shouji_views),
    url(r'^history/',history_views),
    url(r'^coordinates/',coordinates_views,name='history_data'),
    url(r'^query/',query_views),
]
