# Generated by Django 4.2.1 on 2023-05-09 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(blank=True, max_length=25, null=True)),
                ('father_job', models.CharField(blank=True, max_length=25, null=True)),
                ('father_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('name_ar', models.CharField(blank=True, max_length=25, null=True)),
                ('book_price', models.FloatField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=7, null=True)),
                ('hours', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('name_ar', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectYears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.ManyToManyField(to='GPA.subjects')),
                ('year_id', models.ManyToManyField(to='GPA.years')),
            ],
        ),
        migrations.CreateModel(
            name='StuffSubjectYears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.subjectyears')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='StudySchedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('stuff_subject_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.stuffsubjectyears')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubjectYears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.students')),
                ('subject_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.subjectyears')),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='year_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.years'),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField()),
                ('student_subject_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.studentsubjectyears')),
            ],
        ),
        migrations.CreateModel(
            name='Financials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('book_price', models.FloatField(blank=True, null=True)),
                ('date', models.DateField()),
                ('is_purchased', models.SmallIntegerField()),
                ('student_subject_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.studentsubjectyears')),
            ],
        ),
        migrations.CreateModel(
            name='Absences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.students')),
                ('subject_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPA.subjectyears')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
    ]
