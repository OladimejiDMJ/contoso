from django.db import models


class Staffs (models.Model):
    staff_no=models.CharField(max_length=250,blank=True,unique=True)
    first_name=models.CharField(max_length=250,blank=True)
    last_name=models.CharField(max_length=250,blank=True)
    levels=models.CharField(max_length=250,blank=True)
    class_held=models.CharField(max_length=250,blank=True)

    class Meta:
        ordering=['staff_no']
    def __str__(self):
        return '%s %s %s %s' % (self.first_name,self.last_name,self.staff_no,self.class_held)


class Students (models.Model):
    student_no=models.CharField(max_length=250,blank=True,unique=True)
    first_name=models.CharField(max_length=250,blank=True)
    last_name=models.CharField(max_length=250,blank=True)
    student_class=models.CharField(max_length=250,blank=True)

    class Meta:
        ordering=['student_no']
    def __str__(self):
        return '%s %s %s %s' % (self.first_name, self.last_name,self.student_no,self.student_class)


class Teacher_Student (models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE,related_name='num_student')
    teacher=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    
    



# Create your models here.
