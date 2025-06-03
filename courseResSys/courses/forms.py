from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Reservation, Course 

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']     
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })    

#class CourseForm(forms.ModelForm):
    #class Meta:
        #model= Course
        #fields = ['title', 'description', 'start_time', 'end_time', 'capacity','instructor']

#class ReservationForm(forms.ModelForm):
    #class Meta:
        #model= Reservation
        #fields = []   #The user and course are set in the view.   
    #def __init__(self, *args, **kwargs):
        #self.course = kwargs.pop('course', None)
        #self.user = kwargs.pop('user', None)
        #super().__init__(*args,**kwargs)  
    
    #def save(self, commit = True):
        #reservation = super().save(commit=False)
        #reservation.course = self.course
        #reservation.user = self.user
        #if commit :
            #reservation.save()
        #return reservation     
        
                