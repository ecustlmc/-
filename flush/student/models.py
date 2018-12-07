from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    #姓名
    u_name = models.CharField(max_length=20,primary_key=True)
    #密码
    u_password = models.CharField(max_length=20)
    #邮箱
    u_email = models.EmailField(max_length=254)

class Student(models.Model):
    #学号
    s_id = models.CharField(max_length=20,primary_key=True)
    #姓名
    s_name = models.CharField(max_length=20)
    #Jwc密码
    jwc_passwd = models.CharField(max_length = 50)

class Course(models.Model):
    #课程号
    c_id = models.CharField(max_length=20,primary_key=True)
    #课程名
    c_name = models.CharField(max_length=50)

class Score(models.Model):
    #学号
    s_id = models.ForeignKey(Student,to_field='s_id',on_delete=models.CASCADE)
    #课程号
    c_id = models.ForeignKey(Course,to_field='c_id',on_delete=models.CASCADE)
    #分数
    s_score = models.DecimalField(max_digits=4,decimal_places=1)
    #等第
    s_char = models.CharField(max_length=10,default='')

class UserStudent(models.Model):
    #用户名
    u_name = models.ForeignKey(User,to_field='u_name',on_delete=models.CASCADE)
    #学号
    s_id = models.ForeignKey(Student,to_field='s_id',on_delete=models.CASCADE)
    #绑定日期
    a_date = models.DateTimeField()
    #绑定时长
    a_time = models.IntegerField()
    class Meta:
        unique_together = (('u_name','s_id'),)

class Exam(models.Model):
    #考试ID
    e_id = models.CharField(max_length=20,primary_key=True)
    #考试名
    e_name = models.CharField(max_length=50,default='')
    #考试时间
    e_time = models.DateTimeField(default=datetime.datetime(2018,1,1,9,30))
    #考试地点
    e_pos = models.CharField(max_length=50,default = '')


class StudentExam(models.Model):
    #考试ID
    e_id = models.ForeignKey(Exam,to_field='e_id',on_delete=models.CASCADE)
    #考生ID
    s_id = models.ForeignKey(Student,to_field='s_id',on_delete=models.CASCADE)
