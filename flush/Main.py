import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flush.settings")
import django
django.setup()
from student.models import User,Student,UserStudent,Course,Score,Exam,StudentExam
from django.db import connection
from resove import Resove
import SendEmail
#获取所有的学生列表

def compare(newL:list,oldL:list):
    res = []
    for eachNew in newL:
        if eachNew not in oldL:
            res.append(eachNew)
            #print("count = %d target = %d"%(count,target))
    return res


def AllStudentUsers():
    AllStudents = Student.objects.all()
    for eachStudent in AllStudents:
        AllUserStudents = UserStudent.objects.filter(s_id = eachStudent.s_id)
        for eachUserStudent in AllUserStudents:
            eachEmail = User.objects.get(u_name = eachUserStudent.u_name.u_name).u_email
            yield eachStudent.s_id,eachStudent.s_name,eachStudent.jwc_passwd,eachEmail

def main():
    for each in AllStudentUsers():
      try:
        #输出要查询的学生的序号
        print(each)
        #通过视图查询考试信息
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Texam WHERE s_id = {s_id}".format(s_id=each[0]))
            old_rows = cursor.fetchall()
        new_rows = Resove.getExam(each[0],each[1],each[2])#0学号 1姓名 2教务处密码
        #print(new_rows)
        #print(old_rows)
        #
        #比较
        #
        p = compare(new_rows,old_rows)
        #print(p)
        if len(p) != 0:
            #发送邮件
            SendEmail.sendEmail('您的考试信息已经更新！', p, each[3])
        for eachInserRow in p:
            #存储不同
            newE,isCreate = Exam.objects.get_or_create(e_id = eachInserRow[2])
            newE.e_name = eachInserRow[3]
            newE.e_time = eachInserRow[4]
            newE.e_pos = eachInserRow[5]
            newE.save()
            #创建
            StudentExam.objects.create(e_id = newE,s_id = Student.objects.get(s_id = each[0]))
        #
        #检查成绩更新
        #
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Tscore WHERE s_id = {s_id}".format(s_id=each[0]))
            old_rows = cursor.fetchall()
        new_rows = Resove.getScore(each[0],each[1],each[2])#0学号 1姓名 2教务处密码
        #for each in old_rows:
        #   print(each)
        #print("--------------------------------------------------")
        #for each in new_rows:
        #    print(each)
        p = compare(new_rows,old_rows)
        #print(p)
        if len(p) != 0:
            SendEmail.sendEmail('您的教务成绩信息已经更新！',p,each[3])
        for eachInserRow in p:
            #检查课程
            newC,isCreate = Course.objects.get_or_create(c_id = eachInserRow[2])
            newC.c_name = eachInserRow[3]
            newC.save()
            #创建newScore
            Score.objects.create(s_id = Student.objects.get(s_id = each[0]),c_id = newC,s_score = eachInserRow[4],s_char = eachInserRow[5])
      except:
          print(each)
          print("执行出错")
if __name__ == "__main__":
    try:
        main()
    except:
        print("错误,程序终止")
