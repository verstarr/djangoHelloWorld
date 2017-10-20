from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Member(models.Model):

    member_first_name = models.CharField(max_length=200)
    member_last_name = models.CharField(max_length=200)
    member_position = models.CharField(max_length=200)
    member_pbp_chapter = models.CharField(max_length=200)

    member_status = models.BooleanField(False)
    member_picture = models.FileField(max_length=100)

@python_2_unicode_compatible
class Chapter(models.Model):

    chapter_name = models.CharField(max_length=200)
    chapter_location = models.CharField(max_length=200)

    chapter_atb_date = models.DateTimeField('atb date')
