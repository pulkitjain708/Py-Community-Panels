from django.urls import path,include
from .views import loginView

urlpatterns = [
    path('',loginView,name='login'),
]