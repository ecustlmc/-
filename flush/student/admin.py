from django.contrib import admin
from .models import User,Student,Course,Score,UserStudent,Exam,StudentExam
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Score)
admin.site.register(UserStudent)
admin.site.register(Exam)
admin.site.register(StudentExam)

# Register your models here.
