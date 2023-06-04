from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission


# def image_upload(instance, filename):
#     image_name, extension = filename.split(".")
#     return "labs/%s/%s.%s" % (instance.name, instance.name, extension)


class CustomUser(AbstractUser):
    user_gender = (
        ("male", "ذكر"),
        ("female", "أنثى"),)
    gender = models.CharField(
        max_length=10, choices=user_gender, default="male")
    user_religion = (
        ("muslim", "مسلم"),
        ("christsin", "مسيحي"),)
    user_religion = models.CharField(
        max_length=10, choices=user_religion, default="muslim")
    birth_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    nid = models.CharField(max_length=14, null=True, blank=True)
    is_staaff = models.BooleanField(default=False)
    is_admmin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    name_ar=models.CharField(max_length=14, null=True, blank=True)
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=_('groups'),
    #     blank=True,
    #     help_text=_(
    #         'The groups this user belongs to. A user will get all permissions '
    #         'granted to each of their groups.'
    #     ),
    #     related_name='custom_users_groups' # تعيين related_name مخصص للوصول العكسي للحقل groups
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=_('user permissions'),
    #     blank=True,
    #     help_text=_('Specific permissions for this user.'),
    #     related_name='custom_users_permissions' # تعيين related_name مخصص للوصول العكسي للحقل user_permissions
    # )
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)
    def __str__(self):
        return self.username
    