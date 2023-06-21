from django.db import models

# Create your models here.
class Resume(models.Model):
    # first name
    fname = models.CharField(max_length=50)
    # last name
    lname = models.CharField(max_length=50)
    # phone
    phone = models.CharField(max_length=10)
    # email
    email = models.EmailField(max_length=50)
    # skills
    skills = models.TextField()
    # hobbies
    hobbies = models.TextField()
    # createdAt
    createdAt = models.DateTimeField("Created At")
    # updatedAt
    updateAt = models.DateTimeField("Updated At")

