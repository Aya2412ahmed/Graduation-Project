from django.urls import path
from .views import CustomUserSignUpView,login,LoginView
app_name='accounts'
urlpatterns = [
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/",LoginView.as_view(),name="login"),
]