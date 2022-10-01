from django import forms
from urllib import request

from accounts.models import Applicant
from . models import Application, Bursary, BursaryParameter
from  django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

# CHOICES = BursaryParameter.objects.all().values_list('parameter','parameter').distinct()
querry = BursaryParameter.objects.all().values_list('parameter','parameter_value').distinct()

tups = []


for item in querry:
    tups.append(item)

parameters_dict = dict(tups)

# print(parameters_dict)

# choice_list = []

# for item in querry:
#     print(item[0])
#     if item[0] not in choice_list:
#         choice_list.append(item)


class AddBursaryForm(forms.ModelForm):
    class Meta:
        model = Bursary
        fields = '__all__'
        exclude = ['slug']

        widgets = {
            'name_of_bursary' : forms.TextInput(attrs={'class': 'form-control',}),
            'start_date' : forms.DateInput(attrs={'class': 'form-control'}),
            'end_date' : forms.DateInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }

    # labels = {
    #     'name' : _('Hostel Name'),
    #     'rent' : _('Price per room in Ksh'),
    #     'dist' : _('Approximate distance from school'),           
    # }

class AddParameterForm(forms.Form):
    parameter = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=BursaryParameter.objects.all(), required=False)
    

class AddParametersForm(forms.ModelForm):
    class Meta:
        model = BursaryParameter
        fields = ['parameter','parameter_value']

class BursaryParametersForm(forms.ModelForm):

    # field_name = forms.ModelMultipleChoiceField(queryset=ModelClassName.objects.all(),
    #                                        to_field_name='model_class_field_name', 
    #                widget=forms.CheckboxSelectMultiple())

    # choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                   choices=choice_list)

    class Meta:
        model = BursaryParameter
        fields = ['parameter','parameter_value']
        #exclude = ['bursary']

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ['bursary_application','applicant','score']

        widgets = {
            'bursary_application' : forms.TextInput(attrs={'class': 'form-control',}),
            'applicant' : forms.DateInput(attrs={'class': 'form-control',}),
            'score' : forms.TextInput(attrs={'class': 'form-control',}),
        }

