from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=16)
    branch=models.CharField(max_length=100)
    role=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    notesfile=models.FileField()
    filetype=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.sign.signup.user.username+" "+signup.status