from django.contrib import admin
from . models import Category,Course,Lesson,Material,Enrollment,question_answer

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Material)
admin.site.register(Enrollment)
admin.site.register(question_answer)
