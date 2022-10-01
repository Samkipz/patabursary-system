from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from accounts.decorators import unapproved_users
from .models import Application, Bursary, BursaryParameter
from .forms import AddBursaryForm, AddParametersForm, ApplicationForm, BursaryParametersForm
from accounts.models import Applicant
import json


# User = get_user_model()

# Create your views here.
class HomeView(ListView):
    model = Bursary
    template_name = 'home.html'

def bursary_details(request, id=None):
    obj = get_object_or_404(Bursary, id=id)
    queryset = BursaryParameter.objects.exclude(parameter__isnull=True).exclude(parameter__exact='').filter(bursary=obj)
    #SELECT * FROM BursaryParameter WHERE parameter IS NOT NULL AND parameter != ""

    context = {
        "bursary" : obj,
        "parameter" : queryset,
    }
    return render(request, 'bursary_details.html', context)

def Addbursary(request):
    bursary_form = AddBursaryForm(request.POST or None)
    context = {
        "bursary_form" : bursary_form
    }
    if bursary_form.is_valid():
        obj = bursary_form.save(commit=False)
        obj.save()
        return redirect(obj.get_update_url())
        # return redirect('bursaryapp:Editbursary')
    return render(request, 'Addbursary.html', context)

def Addparameters(request, id=None):
    obj = get_object_or_404(Bursary, id=id)
    bursary_form = AddBursaryForm(request.POST or None, instance=obj)
    parameters_form = AddParametersForm(request.POST or None)
    
    querry = BursaryParameter.objects.all().values_list('parameter','parameter_value').distinct()
    tups = []
    for item in querry:
        tups.append(item)
    parameters_dict = dict(tups)    
    print(tups)

    if bursary_form.is_valid and parameters_form.is_valid():
        parent = bursary_form.save(commit=False)
        parent.save()

        param_list = request.POST.getlist('parameter')
        print(param_list)
        val_list = request.POST.getlist('parameter_value')
        

        param_val_list = []

        for item in val_list:
            if item != '':
                param_val_list.append(item)
        
        print(param_val_list)        

        L3 = []
        for x in range(len(param_list)):
            L3.append((param_list[x], param_val_list[x]))

        print(L3)

        param_dict = dict(L3)
        print(param_dict)

        for param in param_dict:
            obj = BursaryParameter()
            obj.parameter = param
            obj.parameter_value = param_dict[param]
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(obj.parameter)
            print(obj.parameter_value)
            if obj.bursary is None:
                obj.bursary = parent
            print(obj)
            obj.save()
            print("Added New Parameters")
        return redirect('accounts:staff_dashboard') 
    context = {
        "bursary" : obj,
        "bursary_form":bursary_form,
        "parameters_form":parameters_form,
        "parameters_dict" : parameters_dict,    
    }
    return render(request, 'Addparameters.html', context)


def Editbursary(request, id=None):
    obj = get_object_or_404(Bursary, id=id)
    bursary_form = AddBursaryForm(request.POST or None, instance=obj)
    ParametersFormset = modelformset_factory(BursaryParameter, form=BursaryParametersForm, extra=0)
    qs = obj.bursaryparameter_set.all()
    formset = ParametersFormset(request.POST or None, queryset=qs)
    context = {
        "bursary_form":bursary_form,
        "formset":formset,
        "object": obj,
    }
    if all([bursary_form.is_valid(), formset.is_valid()]):
        parent = bursary_form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)

            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(child.parameter)
            print(child.parameter_value)
            if child.parameter == None or child.parameter_value == None:
                print("ignore this empty")
            else:
                if child.bursary is None:
                    print("Added New Parameters")
                    child.bursary = parent
                print(child)
                child.save()
        context['message'] = 'Data saved.'
        return redirect('/')
    return render(request, 'Editbursary.html', context)


@login_required(login_url='accounts:login')
@unapproved_users
def applyBursary(request, id=None):
    parent = get_object_or_404(Bursary, id=id,)
    applicant_profile = Applicant.objects.get(user=request.user)
    initial = {'bursary_application': parent, 'applicant':applicant_profile, 'score':'0'}
    applicant_form = ApplicationForm(request.POST or None, initial= initial)
    qs = parent.bursaryparameter_set.all()
    querry = BursaryParameter.objects.filter(bursary_id = parent).values_list('parameter','parameter_value').distinct()

    tups = []


    for item in querry:
        tups.append(item)

    parameters_dict = dict(tups)
    
    context = {
        "bursary" : parent,
        "applicant_form" : applicant_form,
        "applicant_profile":applicant_profile,
        "parameters_dict":json.dumps(parameters_dict),
    }
    if applicant_form.is_valid():
        instance = applicant_form.save(commit=False)
        if Application.objects.filter(bursary_application=instance.bursary_application, applicant=instance.applicant).exists():
            url = request.META.get('HTTP_REFERER', '/')
            resp_body = '<script>alert("You have already applied for this bursary");\
             window.location="%s"</script>' % url
            # messages.info(request, "You have already applied for this bursary")
            print("You have already applied for this bursary")
            return HttpResponse(resp_body)
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(instance.bursary_application)
            print(instance.applicant)
            print(instance.score)
            print(instance,'Succesful.')
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            instance.save()
            context['message'] = 'Application Succesful.'
            return redirect('/')
    return render(request, 'applyBursary.html', context)

def Generateapplicants(request, id=None ):
    obj = get_object_or_404(Bursary, id=id)
    # applicant = Applicant.objects.get(user=request.user)
    applications = Application.objects.filter(bursary_application = obj).order_by('-score')
    context = {
        "bursary":obj,
        "applications":applications,
        # "applicant":applicant,
    }
    return render(request, 'Generateapplicants.html', context)

def Applicants(request):
    applicants = Applicant.objects.all().order_by('user')
    context = {
        "applicants":applicants,
    }
    return render(request, 'Applicants.html', context)