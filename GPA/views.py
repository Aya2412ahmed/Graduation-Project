from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# from .models import MedicalTest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from accounts.models import CustomUser
from .models import Subjects
# from .forms import UpdatePatientForm, DeleteUser, UpdateLapForm, UpdateDoctorForm
from django.contrib.auth import logout, authenticate, login
# Create your views here.

class CoursesList(LoginRequiredMixin,ListView):
    model = Subjects
    context_object_name = 'courses_list'
    template_name='std_dash_board.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Courses Information'  # إضافة متغير إلى السياق
        return context
@login_required
def home(request):
    if request.user.is_staaff:
        context = {}
        return render(request, 'stf_dash_board.html', context)
    elif request.user.is_admmin:
        context = {}
        return render(request, 'admin_dash_board.html', context)
    elif request.user.is_student:
        context = {}
        return render(request, 'std_dash_board.html', context)

