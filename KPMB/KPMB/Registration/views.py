from django.shortcuts import render
from Registration.models import Course, Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new_course(request):
    if request.method == "POST":
        c_code = request.POST['code']
        c_desc = request.POST['description']
        data = Course(code=c_code, description=c_desc)
        data.save()
        return render(request, 'new_course.html', {'message':'Data Save'})
    else:
        return render(request, 'new_course.html')

def course(request):
    allcourse = Course.objects.all() 
    dict = {
        'allcourse': allcourse
    }
    return render(request,'course.html', dict)

def search_course(request):
    if request.method == 'GET':
        data = Course.objects.filter(code = request.GET.get ('c_code'))
        dict = {
            'data' : data
        }
        return render(request, 'search_course.html', dict)
    else:
        return render(request, 'search_course.html')

def update_course(request,code): # code= data code dr course.html
    data = Course.objects.get(code=code) #code dlm database 1, code dr course.html (Data.code)
    dict = {
        'data' : data
    }
    return render(request, 'update_course.html', dict)

def save_update_course(request, code):
    c_desc = request.POST['description']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))

def new_student(request):
    data2 = Course.objects.all() 

    if request.method == "POST":
        #GET DATA FROM HTML FILE
        Id = request.POST['s_id'] #dlm bracket name from html 
        Name = request.POST['s_name']
        Address = request.POST['s_address']
        Phone = request.POST['s_phone']
        S_Code = request.POST['code']


        #GET FK FROM TABLE
        data_course = Course.objects.get(code = S_Code)

        #ASSIGN VALUE DATA
        data = Student(id = Id, name = Name, address = Address, phone = Phone, course_code = data_course)

        #SAVE DATA
        data.save()

        dict = {
            'code': data2,
            'message': "Data Save"
        }
    else:
        dict = {
            'code': data2
        }
    return render(request,'new_student.html', dict) #dic nk antar value kat html

def searchby_student(request):
    if request.method == "POST":
        s_id = request.POST['s_id']
        data_student = Student.objects.get(id = s_id)
        data = Course.objects.get(code = data_student.course_code_id)
        dict = {
            'data_student': data_student,
            'desc': data.description
        }
        return render(request, 'searchby_student.html', dict)

    else:
        return render(request, 'searchby_student.html') #xclick button (stay on that page)

def searchby_course(request):
    c_code = Course.objects.all() 
    if request.method == "GET":
        stud_course = Student.objects.filter(course_code=request.GET.get('s_course'))
        dict = {
            'stud_list':stud_course,
            'course':request.GET.get('s_course'),
            'c_code':c_code
        }
    else:
        dict = {
            'c_code': c_code
        }
        return render(request, 'searchby_course.html', dict)