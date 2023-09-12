from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.

# HOME
def home(request):
    students = Student.objects.all()

    context = {
        'students':students
    }
    return render(request,'home.html', context)

# VIEW STUDENT 
def view_student(request, pk):
    student = Student.objects.get(id=pk)

    context = {
        'student': student
    }
    return render(request,'view.html', context)


# All STUDENTS
def all_students(request):
    students = Student.objects.all()

    context = {
        'students' : students
    }
    return render(request,'all_students.html', context)


# CREATE STUDENT
def create_student(request):
    form  = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'form' : form
    }
    return render(request,'create_student.html', context)


# UPDATE STUDENT
def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'update.html', context)
        


# DELETE STUDENT
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')

    context = {
        'student': student
    }
    return render(request,'delete.html', context)