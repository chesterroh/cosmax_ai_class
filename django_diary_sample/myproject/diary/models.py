from django.db import models

# Create your models here.

class Entry(models.Model):
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date input')
    def __str__(self):
        return self.subject
        