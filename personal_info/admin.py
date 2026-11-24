from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'last_name', 'first_name', 'course', 'year_level', 'enrollment_status')
    list_filter = ('enrollment_status', 'course', 'year_level')
    search_fields = ('student_id', 'first_name', 'last_name', 'course')
