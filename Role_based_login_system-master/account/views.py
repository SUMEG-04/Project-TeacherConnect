from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import User
from .models import Database
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_subadmin:
                login(request, user)
                return redirect('subadmin')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    teacher_db = Database.objects.all()
    colleges_db = teacher_db.order_by().values('college').distinct()
    dept_db = teacher_db.order_by().values('subject').distinct()
    # print(teacher_db)
    return render(request,'admin.html', {'all_teacher': teacher_db, 'all_colleges': colleges_db, 'all_dpts': dept_db})


def subadmin(request):
    return render(request,'subadmin.html')

def teacher(request):
    return render(request,'teacher.html')

def search(request):
    users = User.objects.all()
    return render(request , 'search.html',{'users':users})

def take_input(request):
    emp_id = request.POST.get("EmpID")
    user_name = request.POST.get("username")
    mail_id = request.POST.get("email")
    college_name = request.POST.get("college")
    subject_name = request.POST.get("subject")
    designation = request.POST.get("designation")
    # is_phd = request.POST.get("isphd")
    newinput = Database(EmpID = emp_id,username =  user_name , email = mail_id, college = college_name, subject = subject_name , designation = designation) 
    newinput.save()
    return redirect('show_teachers')


def show_teachers(request):
    context = {
        "all_data" : Database.objects.all(),
    }
    return render(request,"show_teachers.html",context = context)

def search_teachers(request):
    search_t = request.POST.get('search_t')
    whole_data = Database.objects.all()
    context = {
        "all_data" : whole_data.filter(Q(username__contains = search_t))

    }
    return render(request, "show_teachers.html",context = context)

def edit(request):
    context = {
        "all_data" : Database.objects.all(),
    }
    return render(request,"show_teachers.html",context = context)

def update(request,id):
        emp_id = request.POST.get("EmpID")
        user_name = request.POST.get("username")
        mail_id = request.POST.get("email")
        college_name = request.POST.get("college")
        subject_name = request.POST.get("subject")
        designation = request.POST.get("designation")
        # is_phd = request.POST.get("isphd")
        newinput = Database(id = id ,EmpID = emp_id,username =  user_name , email = mail_id, college = college_name, subject = subject_name , designation = designation) 
        newinput.save()
        return redirect('show_teachers')
    
    

def delete(request,id):
    data = Database.objects.filter(id = id)
    data.delete()

    return redirect('show_teachers')