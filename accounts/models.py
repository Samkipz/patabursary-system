import os
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_applicant = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_no = models.CharField(_('phone number'), max_length=15, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name+' '+self.last_name


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True, related_name='applicant_profile')
    registration_number = models.CharField(max_length=100, unique=True)
    id_number = models.CharField(_('National ID number/Passport'),max_length=15,null=True)
    county = models.CharField(max_length=500, null=True)
    number_of_siblings = models.IntegerField(null=True)
    parents_occupation = models.CharField(max_length=500,null=True)
    family_mothly_income = models.IntegerField(null=True)
    STUDY_YEAR = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
    )
    year_of_study = models.CharField(max_length=1, choices=STUDY_YEAR)
    course_name = models.CharField(max_length=300)
    MARITIAL_STATUS = (
        ('Married', 'Married'),
        ('Single', 'Single'),
    )
    maritial_status = models.CharField(max_length=15, choices=MARITIAL_STATUS)
    STUDENT_CATEGORY = (
        ('GSSP', 'GSSP'),
        ('PSSP Degree', 'PSSP Degree'),
        ('PSSP Diploma', 'PSSP Diploma'),
    )
    student_category = models.CharField(max_length=15, choices=STUDENT_CATEGORY, default='GSSP')
    death_cert_father = models.FileField(_('Death Certificate of Father'), upload_to='pics', blank=True)
    death_cert_mother = models.FileField(_('Death Certificate of Mother'), upload_to='pics', blank=True)
    performance = models.FileField(_('Latest transript'), upload_to='pics', blank=True)
    disabled = models.BooleanField(_('Do You have any disability'), default=False)
    avatar = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    fee_balance = models.IntegerField(null=True)
    approved = models.BooleanField(default=False)
    

    def __str__(self):
            return str(self.user)

    def get_avatar(self):
        if not self.avatar:
            return "/media/profile_pics/default-profile.png"
        else:
            return os.path.join(settings.MEDIA_URL, self.avatar.name)

    @property 
    def percentage_complete(self):
        #b = [student.user_name.f1, user.user_name.f2, user.user_name.f3, user.user_name.f4, user.user_name.f5]
        percent = {'student.first_name': 20, 'registration_number': 20, 'year_of_study': 20, 'gender': 20, 'course_name': 20, 'maritial_status': 20 }
        total = 0
        if self.registration_number:
            total += percent.get('registration_number', 0)
        if self.year_of_study:
            total += percent.get('year_of_study', 0)
        if self.gender:
            total += percent.get('gender', 0)
        if self.course_name:
            total += percent.get('course_name', 0)
        if self.maritial_status:
            total += percent.get('maritial_status', 0)
        return total

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='staff_profile')
    staff_pin = models.IntegerField(_('Enter Pin'), null=True, unique=True)

    def __str__(self):
            return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.is_applicant:
        Applicant.objects.get_or_create(user = instance)
    else:
        Staff.objects.get_or_create(user = instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('_-----')	
    # print(instance.internprofile.bio, instance.internprofile.location)
    if instance.is_applicant:
        instance.applicant_profile.save()
    else:
        Staff.objects.get_or_create(user = instance)