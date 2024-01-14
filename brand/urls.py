from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_brand, name='add_brand'),
    # path('add/', views.AddBrand.as_view(), name='add_brand'),
]