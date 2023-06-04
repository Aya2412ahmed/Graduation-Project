from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import CreateView
from .forms import CustomUserCreationForm,LoginForm
# Create your views here.
class CustomUserSignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"

# class MyLoginView(LoginView):
#     template_name = 'registration/login.html'
def login(request):
    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['password'].widget.attrs['class'] = "form-control"
    form.fields['username'].label = ""
    form.fields['password'].label = ""
    if request.method == 'POST':
        
        form = AuthenticationForm(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('GPA:login_home'))
        else:
            error_message = "Invalid username or password."
        
    else:
        form = AuthenticationForm()
        error_message = None
    return render(request, "registration/login.html",  {'form': form, 'error_message': error_message})

class LoginView(View):
    template_name = 'registration/login.html'
    
    def get(self, request):
        form = AuthenticationForm()
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password'].widget.attrs['class'] = "form-control"
        form.fields['username'].label = ""
        form.fields['password'].label = ""
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password'].widget.attrs['class'] = "form-control"
        form.fields['username'].label = ""
        form.fields['password'].label = ""
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('GPA:login_home')
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid username or password."

        return render(request, self.template_name, {'form': form, 'error_message': error_message})