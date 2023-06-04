from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Subjects(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    name_ar = models.CharField(max_length=25, null=True, blank=True)
    book_price = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=7, null=True, blank=True)
    hours = models.PositiveIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.name)


class Years(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    name_ar = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class SubjectYears(models.Model):
    subject_id = models.ManyToManyField(Subjects)
    year_id = models.ManyToManyField(Years)
    def __str__(self):
        return str(self.subject_id.name)

class StuffSubjectYears(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject_year_id = models.ForeignKey(SubjectYears, on_delete=models.CASCADE)


class StudySchedules(models.Model):
    stuff_subject_year_id = models.ForeignKey(
        StuffSubjectYears, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        return str(self.start_time)

class Students (models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    year_id = models.ForeignKey(Years,  on_delete=models.CASCADE)
    family_name = models.CharField(max_length=25, null=True, blank=True)
    father_job = models.CharField(max_length=25, null=True, blank=True)
    father_phone = models.CharField(max_length=11, null=True, blank=True)
    def __str__(self):
        return str(self.user_id.first_name)

class StudentSubjectYears (models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_year_id = models.ForeignKey(SubjectYears, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.student_id.user_id.first_name)

class Results(models.Model):
    student_subject_year_id = models.ForeignKey(
        StudentSubjectYears, on_delete=models.CASCADE)
    gpa = models.FloatField()
    def __str__(self):
        return str(self.gpa)


class Financials(models.Model):
    student_subject_year_id = models.ForeignKey(
        StudentSubjectYears, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField()
    price = models.FloatField()
    book_price = models.FloatField(null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    is_purchased = models.SmallIntegerField()
    def __str__(self):
        return str(self.price)


class Absences(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_year_id = models.ForeignKey(SubjectYears, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.date)
