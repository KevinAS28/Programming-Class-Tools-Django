from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    index = models.IntegerField(blank=False, null=False, default=0)
    kelas = models.CharField(max_length=15, default=" --- ")
    
    def __str__(self):

        return self.name
        