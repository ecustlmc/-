from django.shortcuts import render,HttpResponse
from .forms import UserForm,AddStudent
from .models import User,Student,UserStudent
import datetime
def admin(request):
    f = UserForm(request.POST)
    if request.method == "POST":
        if f.is_valid():
            data = f.clean()
            u_id = data.get("u_id")
            u_pd = data.get("u_pd")
            u_email = data.get("u_email")
            pd = data.get("pd")
            if pd != 'ecust':
                return render(request,"AddUser.html",{"f":f,'result':'密令错误'})
            try:
                (newUser,isCreate) = User.objects.get_or_create(u_name=u_id, u_password=u_pd, u_email=u_email)
                if isCreate:
                    return render(request,"AddUser.html",{"f":f,'result':'添加成功'})
            except:
                f = UserForm()
                return render(request,"AddUser.html",{"f":f,'result':'添加失败'})
        return render(request,"AddUser.html",{"f":f,'result':'cstoken错误'})
    else:
        return render(request,'AddUser.html',{'f':f})


# Create your views here.
def adminUS(request):
    f = AddStudent(request.POST)
    if request.method == "POST":
        if f.is_valid():
            data = f.clean()
            u_id = data.get("u_id")
            s_id = data.get("s_id")
            s_name = data.get("s_name")
            pd = data.get("pd")
            jwc_pwd = data.get("jwc_pwd")
            if pd != 'ecust':
                return render(request,"AddStudent.html",{"f":f,'result':'密令错误'})
            #try:
            #检查当前学号是否存在
            newS,StudentIsCreate = Student.objects.get_or_create(s_name = s_name,s_id = s_id,jwc_pwd=jwc_pwd)
            #检查当前用户是否存在,不存在会报错
            try:
                ExistUser = User.objects.get(u_name = u_id)
            except:
                return render(request,"AddStudent.html",{"f":f,'result':'该账号不存在'})
            #创建了新学生
            if StudentIsCreate:
                newUS,isC = UserStudent.objects.get_or_create(u_name = ExistUser, s_id = newS, a_date = datetime.datetime.now(),a_time = 1)
                if isC:
                    return render(request,"AddStudent.html",{"f":f,'result':'添加学生和关系成功'})
                else:
                    return render(request,"AddStudent.html",{"f":f,'result':'已经添加过该关系'})
            #没有创建新学生
            if not StudentIsCreate:
                #当前学号存在，则只添加关系
                try:
                    newUS,isC = UserStudent.objects.get_or_create(u_name = ExistUser, s_id = newS, a_date = datetime.datetime.now(),a_time = 1)
                except:
                    return render(request,"AddStudent.html",{"f":f,'result':'已经添加过该关系'})
                if isC:
                    return render(request,"AddStudent.html",{"f":f,'result':'添加关系成功'})
                else:
                    return render(request, "AddStudent.html", {"f": f, 'result': '已经添加过该关系'})
        return render(request,"AddStudent.html",{"f":f,'result':'cstoken错误'})
    else:
        return render(request,'AddStudent.html',{'f':f})