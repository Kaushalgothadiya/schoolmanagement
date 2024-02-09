from django.contrib import admin
from .models import Student,Section,Product,Items,Course
# Register your models here.

admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Items)
admin.site.register(Course)
