from django.contrib import admin
from .models import Reservation, Course
from django.contrib.auth import get_user_model
# Register your models here.
admin.site.register(get_user_model())
admin.site.register(Course)
admin.site.register(Reservation)