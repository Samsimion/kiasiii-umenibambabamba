from django.contrib import admin
from .models import SchoolCategory, PrimarySchool,HighSchool

# Register your models here.


admin.site.register(SchoolCategory)
admin.site.register(PrimarySchool)
admin.site.register(HighSchool)


