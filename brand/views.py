from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
def add_brand(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('add_brand')
    
    else:
        brand_form = forms.BrandForm()
    return render(request, 'add_brand.html', {'form': brand_form})

# class AddBrand(CreateView):
#     form_class = forms.BrandForm
#     template_name = 'add_brand.html'
#     success_url = reverse_lazy('add_brand')