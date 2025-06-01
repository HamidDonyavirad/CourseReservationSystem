from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_list, name='home'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/reserve/', views.reserve_course, name='reserve_course'),
    path('my-reservations/', views.my_reservations,name='my_reservations'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]