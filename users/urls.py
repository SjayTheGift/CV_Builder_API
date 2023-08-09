from django.urls import path
from .views import (
    LogInView, 
    RegisterUserView,
)

urlpatterns = [
      path('api/user/login/', LogInView.as_view(), name='login'),
      path('api/user/register/', RegisterUserView.as_view(), name='register'),
]
