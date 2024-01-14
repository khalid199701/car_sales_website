from django.urls import path
from . import views
urlpatterns = [
    # path('add/', views.add_car, name='add_car'),
    path('add/', views.AddCar.as_view(), name='add_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
    path('details/purchase/<int:id>/', views.purchase_car, name='purchase_car'),
]
