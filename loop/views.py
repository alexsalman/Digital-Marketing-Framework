from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Company


class IndexView(generic.ListView):
    template_name = 'loop/index.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return Company.objects.all()

class DetailView(generic.DetailView):
    model = Company
    template_name = 'loop/detail.html'

class CompanyCreate(CreateView):
    model = Company
    fields = ['market_name', 'unique_name', 'overview', 'founded_year', 'phone_number', 'email_address', 'website_url',
            'company_logo', 'address_country', 'address_state', 'address_city', 'address_zip', 'address_street', 'address_postal']

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['market_name', 'unique_name', 'overview', 'founded_year', 'phone_number', 'email_address', 'website_url',
            'company_logo', 'address_country', 'address_state', 'address_city', 'address_zip', 'address_street', 'address_postal']

class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('loop:index')
