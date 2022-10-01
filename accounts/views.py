from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib import auth, messages
from django.utils.translation import gettext_lazy as _
from accounts.forms import ApplicantUpdateForm, MyUserCreationForm, UserForm

from accounts.models import Applicant

User = get_user_model()
#register user
def registerView(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = MyUserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})
    
#login user
def loginView(request):
    if request.method == 'POST':
        email = request.POST.get("email", "default value")
        password = request.POST.get("password", "default value")

        user = auth.authenticate(request, email = email, password = password)

        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
            # if user.is_staff:
            #     auth.login(request,user)
            #     if 'next' in request.POST:
            #         return redirect(request.POST.get('next'))
            #     else:
            #         return redirect('/')
            # else:
            #     auth.login(request,user)
            #     if 'next' in request.POST:
            #         return redirect(request.POST.get('next'))
            #     else:
            #         return redirect('/')
        else:
            messages.error(request,'Your Username or Password is incorrect')
    # else:
    context = {}
    return render(request,'accounts/login.html', context)

def staff_dashboard(request):
    return render(request, 'accounts/staff_dashboard.html')

def applicant_dashboard(request):
    applicant = Applicant.objects.get(user=request.user)
    context = {
        "applicant":applicant,
    }
    return render(request, 'accounts/applicant_dashboard.html', context)

def applicant_profile(request, id=None):
    applicant=Applicant.objects.get(id=id)
    context = {
        "applicant":applicant,
    }
    return render(request, 'accounts/applicant_profile.html', context)


def update_profile(request):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)

        try:
            applicant_profile = Applicant.objects.get(user=request.user)
            profile_form = ApplicantUpdateForm(request.POST, request.FILES, instance=applicant_profile)
            # if it's a OneToOne field, you can do:
            # profile = request.user.myprofile

        except Applicant.DoesNotExist:
            applicant_profile = None
            profile_form = ApplicantUpdateForm(request.POST)
            # applicant_profile = Applicant.objects.get(user = request.user)
            # profile_form = ApplicantUpdateForm(request.POST, instance=applicant_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('accounts:applicant_dashboard')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)

        try:
            applicant_profile = Applicant.objects.get(user=request.user)
            profile_form = ApplicantUpdateForm(instance=applicant_profile)
            # if it's a OneToOne field, you can do:
            # profile = request.user.myprofile

        except Applicant.DoesNotExist:
            applicant_profile = None
            profile_form = ApplicantUpdateForm()

        # applicant_profile = Applicant.objects.get(user_id=request.user.id)
        # profile_form = ApplicantUpdateForm(request.POST, instance=applicant_profile)
    	
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
	})

def approve(request,id=None):
    applicant=Applicant.objects.get(id=id)
    applicant.approved=True
    applicant.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




    
    

