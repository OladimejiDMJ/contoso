from django.contrib import admin
from .models import Staffs,Students,Teacher_Student
@admin.register(Staffs)
class StaffsAdmin(admin.ModelAdmin):
    list_display=("staff_no","first_name","last_name","class_held","levels")
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=("student_no","first_name","last_name","student_class")


@admin.register(Teacher_Student)
class Teacher_Student_Admin(admin.ModelAdmin):
    pass
# Register your models here.
