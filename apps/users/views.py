from django.shortcuts import render


# 创建from的相应views逻辑
def Xadmin_testGet_from(request):

    return render(request, 'from.html')
