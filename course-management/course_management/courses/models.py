from django.db import models
# from django.contrib.admindocs import value_to_string


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_date = models.DateField(max_length=30)
    end_date = models.DateField(max_length=30)
    approximation = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    lection_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    week = models.CharField(max_length=30)
    course = models.ForeignKey(Course)
    url = models.CharField(max_length=30)

