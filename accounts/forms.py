from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import Applicant, Staff, User

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name','last_name','email', 'phone_no')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email', 'phone_no')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_no')

class ApplicantUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields =  fields = ('registration_number', 'year_of_study', 'course_name', 'maritial_status', 'death_cert_father', 'death_cert_mother', 'disabled', 'fee_balance')
        
class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('staff_pin',)
