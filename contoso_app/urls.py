from django.urls import path
from . import views
urlpatterns = [
    path('new_staff/', views.new_staff, name='new_staff'),
    path('new_student/',views.new_student,name='new_student'),
    path('student_teacher/',views.student_per_teacher,name='student_per_teacher'),
 ]
