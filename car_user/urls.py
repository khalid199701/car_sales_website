from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('user_login/', views.user_login, name='user_login'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('profile/', views.profile, name='profile'),
    # path('logout/', views.user_logout, name='user_logout'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]