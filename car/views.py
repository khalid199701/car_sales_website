from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return redirect('add_car')
    else:
        car_form = forms.CarForm()
    return render(request, 'add_car.html', {'form': car_form})

class AddCar(CreateView):
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car.html')

    
class DetailCarView(View):
    
    template_name = 'car_details.html'

    def get(self, request, *args, **kwargs):
        car_id = self.kwargs.get('id')
        car = models.Car.objects.get(id=car_id)
        comment_form = forms.CommentForm()
        comments = car.comments.all()

        context = {
            'car': car,
            'comment_form': comment_form,
            'comments': comments,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()  # Use 'car' instead of 'post'
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car  # Use 'car' instead of 'post'
            new_comment.save()
        
        if request.user.is_authenticated:
            # Check if the car is available for purchase
            if car.quantity > 0 and car.purchased_by is None:
                # Update the car's purchased_by field
                car.purchased_by = request.user
                car.quantity -= 1
                car.save()
            
        return self.get(request, *args, **kwargs)
        
    
@login_required
def purchase_car(request, id):
    car = models.Car.objects.get(id=id)

    # Check if the car is available for purchase
    if car.quantity > 0 and car.purchased_by is None:
        # Update the car's purchased_by field
        car.purchased_by = request.user
        car.quantity -= 1
        car.save()

    return redirect('car:detail_car', id=id)