from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Reservation
from .forms import  UserCreationForm
from django.contrib import messages
from django.contrib.auth import login , logout
from .forms import CustomLoginForm


#Show course list (Course)
def course_list (request):
    courses = Course.objects.all()
    return render(request,'home.html', {'courses': courses})

#Show details of each course
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    is_reserved = False

    if request.user.is_authenticated:
        is_reserved = Reservation.objects.filter(user=request.user, course=course).exists()

        if request.method == 'POST' and not is_reserved:
            Reservation.objects.create(user=request.user, course=course)
            is_reserved = True  
            return redirect('course_detail', course_id=course.id)  

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_reserved': is_reserved,
    })

    
#View user's booked courses
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).select_related('course')
    return render(request, 'courses/my_reservations.html', {'reservations': reservations})
   
#Register user 
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
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'The username or password is incorrect.')
    else:
        form = CustomLoginForm()        
    return render(request, 'login.html', {'form': form})         

@login_required
def logout_view(request):
    logout(request)
    return redirect('home') 
  
#delete the reserved course 
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == "POST":
        reservation.delete()
        return redirect('my_reservations')  
    return redirect('my_reservations')          