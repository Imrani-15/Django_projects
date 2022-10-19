from django.db import models

# Create your models here.
class StudentFeedback(models.Model):
    Firstname = models.CharField(max_length=100)
    Secondname = models.CharField(max_length=100)
    Phonenumber = models.IntegerField()
    EmailId = models.EmailField()
    Feedback = models.TextField()
