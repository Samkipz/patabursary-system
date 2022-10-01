from xml.parsers.expat import model
from django.db import models
from django.urls import reverse
# from pbursary.util import unique_slug_generator
from django.db.models.signals import pre_save

from accounts.models import Applicant
# from django.dispatch import receiver

# Create your models here.
class Bursary(models.Model):
    name_of_bursary = models.CharField(max_length=300)
    start_date = models.DateField(auto_now_add = False, auto_now = False)
    end_date = models.DateField(auto_now_add = False, auto_now = False)
    description = models.TextField()
    # slug = models.SlugField(null=False, unique=True, blank=True)

    def __str__(self):
        return self.name_of_bursary
    
# @receiver(pre_save, sender= Bursary)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


    def get_absolute_url(self):
        return reverse("bursaryapp:Addbursary", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("bursaryapp:Addparameters", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("bursaryapp:Editbursary", kwargs={"id": self.id})

    def get_parameters_children(self):
        return self.bursaryparameter_set.all()

class BursaryParameter(models.Model):
    bursary = models.ForeignKey(Bursary,on_delete=models.CASCADE, null=True)
    parameter = models.CharField(max_length=300, null=True)
    parameter_value = models.IntegerField(null=True)

    def __str__(self):
        if self.parameter:
            return self.parameter + ' - '+ str(self.bursary)
        else:
            return 'empty parameter'

    def get_absolute_url(self):
        return self.bursary.get_absolute_url()
        
class Application(models.Model):
    bursary_application = models.ForeignKey(Bursary,on_delete=models.CASCADE, null=True)
    applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE, null=True)
    date_of_application = models.DateTimeField(auto_now_add=True, auto_now=False)
    score = models.IntegerField(default=0)
    status = models.BooleanField(null=True)

    def __str__(self):
            return str(self.applicant) +' application for '+  str(self.bursary_application)

            