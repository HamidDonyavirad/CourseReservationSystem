from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Reservation
from .forms import ReservationForm, CourseForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


#Show course list (Course)
def course_list (request):
    courses = Course.objects.all()
    return render(request,'courses/course_list.html', {'courses': courses})

#Show details of each course
def course_detail(request,course_id):
   course = get_object_or_404(Course,id = course_id) 
   is_reserved = Reservation.objects.filter(user=request.user, course=course).exists()
   return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_reserved': is_reserved,
        })
   
#Course reservation for students only
@login_required
def reserve_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user, course = course)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Reservation was successful.')
            except:
                messages.error(request,'You have already booked this course.')
            return redirect('course_detial', course_id=course.id)
    else:
        form = ReservationForm(user = request.user, course=course)
    return render(request, 'courses/reserve_course.html', {
        'form': form,
        'course': course
    })
    
#View user's booked courses
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).select_related('course')
    return render(request, 'courses/my_reservations.html', {'reservations': reservations})

#Creating a new course only by the instructor
@login_required
def course_create(request):
    if request.user.role != 'instructor':
        return HttpResponseForbidden('You are not allowed to create courses.')
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm()
    
    return render(request, 'courses/course_form.html', {'form': form})

#Seeing students in a specific course
@login_required
def course_students(request,course_id):
    course = get_object_or_404(course, id=course_id)
    if course.instructor != request.user:
        return HttpResponseForbidden('You are not authorized to view this list.')
    students = Reservation.objects.filter(course=course).select_related('user')
    return render(request,'courses/course_students.html', {
        'course': course,
        'students': students
    })

#course_update
@login_required
def course_update(request, course_id):
    course = get_object_or_404(Course, id=course_id) 
    if course.instructor != request.user:
        return HttpResponseForbidden('You are not authorized to view this list.')
    if request.method == 'POST':
        form = CourseForm(request.POST, instance= course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id = course.id)
    else:
        form = CourseForm(instance=course) 
    return render(request, 'courses/course_form.html', {'form': form, 'course': course})

#course_delete
@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.instructor != request.user:
        return HttpResponseForbidden('You are not authorized to view this list.')
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course successfully deleted.')  
        return redirect('course_list')  
    return render(request, 'courses/course_confirm_delete.html', {'course': course}) 

#Show student list
@login_required
def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user != course.instructor:
        return HttpResponseForbidden("You are not authorized to view this list.")

    reservations = Reservation.objects.filter(course=course).select_related('user')

    return render(request, 'courses/course_students.html', {
        'course': course,
        'reservations': reservations
    }) 
    
    
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
            return redirect('course_list')  
        else:
            messages.error(request, 'The username or password is incorrect.')
    else:
        form = AuthenticationForm()        
    return render(request, 'login.html', {'form': form})         

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')             