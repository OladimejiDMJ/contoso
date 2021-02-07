from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher_Student

# # Create your views here.
from .forms import StaffForm,StudentForm
def new_staff(request):
    if request.method=='POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponse('New Staff successfully added')
    else:
        form = StaffForm()

    return render(request, 'staff.html', {'form': form})
def new_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            post=form.save()
            post.save()
            return HttpResponse('New Student successfully added')
    else:
        form=StudentForm()
    return render(request, 'student.html', {'form': form})
def student_per_teacher(request):
    records=Teacher_Student.objects.all()
    store=dict()
    for record in records:
        teacher=record.teacher
        if not store.get(teacher):
            store[teacher]=list()
        store[teacher].append(record.student)
    return HttpResponse(store[teacher])


# def student_per_teacher():
#      records=Teacher_Student.objects.all()
#      return(records)
         


