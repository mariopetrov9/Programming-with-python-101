from django.contrib import admin
from .models import Course, Lecture


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "description",
                    "start_date",
                    "end_date",
                    "approximation")


admin.site.register(Course, CourseAdmin)


class LectureAdmin(admin.ModelAdmin):
    list_display = ("lection_id",
                    "name",
                    "week",
                    "course",
                    "url")


admin.site.register(Lecture, LectureAdmin)
