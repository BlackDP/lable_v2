from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest


# Create your views here.

from .models import UserProfile


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        profile = UserProfile.objects.get_or_create(name_id=self.request.user.id)
        context['profile'] = profile
        return context