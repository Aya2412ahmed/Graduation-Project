from django.contrib import admin
from .models import Subjects,Years,SubjectYears,StuffSubjectYears,StudySchedules,Students,StudentSubjectYears,Results,Financials,Absences
# Register your models here.
admin.site.register(Subjects)
admin.site.register(Years)
admin.site.register(SubjectYears)
admin.site.register(StuffSubjectYears)
admin.site.register(StudySchedules)
admin.site.register(Students)
admin.site.register(StudentSubjectYears)
admin.site.register(Results)
admin.site.register(Financials)
admin.site.register(Absences)