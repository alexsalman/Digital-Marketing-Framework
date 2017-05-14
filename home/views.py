from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from loop.models import Company

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        companies = Company.objects.all()
        args = { 'users' : users, 'companies' : companies }
        return render(request, self.template_name, args)
