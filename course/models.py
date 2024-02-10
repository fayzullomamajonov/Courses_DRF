from django.db import models

# Create your models here.

class CourseModel(models.Model):
    name = models.CharField(max_length=15)
    month = models.IntegerField()
    day = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    