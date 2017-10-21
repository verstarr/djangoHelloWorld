from django.contrib import admin

from .models import Chapter, Member

# Register your models here.
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': ['member_first_name',
                                             'member_last_name',
                                             'member_position',
                                             'member_pbp_chapter']}),
        ('Pbp Member Information', {'fields': ['member_status',
                                               'member_picture']}),
    ]