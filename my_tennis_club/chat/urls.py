from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.chat_view, name='home'),
    path('api/newdata/', views.new_data, name='newdata'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
