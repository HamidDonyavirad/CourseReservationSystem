from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/reserve/', views.reserve_course, name='reserve_course'),
    path('my-reservations/', views.my_reservations,name='my_reservations'),
    path('create/', views.course_create, name='course_create'),
    path('<int:course_id>/students/', views.course_students, name='course_students'),
    path('<int:course_id>/edit/', views.course_update, name='course_update'),
    path('<int:course_id>/delete/', views.course_delete, name='course_delete'),
    
]