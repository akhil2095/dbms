from django.contrib import admin
from myapp.models import UserProfile, Course

class StudentAdmin(admin.ModelAdmin):
	model = Course
	filter_horizontal = ('students',)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course, StudentAdmin)
