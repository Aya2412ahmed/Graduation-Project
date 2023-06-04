from django.contrib import admin
from django.urls import path
from .views import home,CoursesList

app_name="GPA"

urlpatterns = [
    path('',home,name='login_home' ),
    path('courses/',CoursesList.as_view(),name='courses' ),
    
    
]