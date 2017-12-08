from django.conf.urls import url
from django.contrib import admin
from apps.users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 为from创建一个URL映射
    url(r'^from/', views.Xadmin_testGet_from, name="Xadmin_testGet_from"),

]