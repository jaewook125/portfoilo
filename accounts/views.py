from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.db import transaction
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy #success_url 활용 될때 순차적으로 실행하지않고 "게으르게" 실행
from .forms import UserCreationForm, ProfileForm
import logging

User = get_user_model()

signup = CreateView.as_view(model=User, form_class=UserCreationForm,
							template_name='accounts/signup_form.html',
							success_url=reverse_lazy('root')) 
							#success_url이 활용이 될때 root실행



@login_required
def profile(request):
	return render(request, 'accounts/profile.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid(): # 유저폼과 프로필검수
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('accounts:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserCreationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })