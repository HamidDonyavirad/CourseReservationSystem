from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Reservation
from .forms import ReservationForm, CourseForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm


#Show course list (Course)
def course_list (request):
    courses = Course.objects.all()
    return render(request,'home.html', {'courses': courses})

#Show details of each course
def course_detail(request,course_id):
   course = get_object_or_404(Course,id = course_id) 
   is_reserved = False
   if request.user.is_authenticated:
        is_reserved =Reservation.objects.filter(user=request.user, course=course).exists()
   return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_reserved': is_reserved,
        })
   
#Course reservation for students only
@login_required
def reserve_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_reservations = Reservation.objects.filter(user=request.user).select_related('course')
    
    if request.method == 'POST':
        if Reservation.objects.filter(user=request.user, course=course).exists():
            messages.error(request, 'You have already booked this course.')
            return redirect('course_detail', course_id= course.id)
        form = ReservationForm(request.POST, user=request.user, course = course)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Reservation was successful.')
            except:
                messages.error(request,'You have already booked this course.')
            return redirect('course_detail', course_id=course.id)
    else:
        form = ReservationForm(user = request.user, course=course)
    return render(request, 'courses/reserve_course.html', {
        'form': form,
        'course': course,
        'user_reservations': user_reservations
    })
    
#View user's booked courses
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).select_related('course')
    return render(request, 'courses/my_reservations.html', {'reservations': reservations})
   
#Register user and instructor
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration completed successfully.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})    

 #login user and instructor 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'The username or password is incorrect.')
    else:
        form = AuthenticationForm()        
    return render(request, 'login.html', {'form': form})         

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')             