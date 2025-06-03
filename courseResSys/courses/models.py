from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User (AbstractUser):
    pass
    
class Course (models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)    
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Reservation (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user','course')
             

    def __str__(self):
        return f"{self.user.username} -> {self.course.title}"