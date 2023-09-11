from django.db import models

# Create your models here.

class Child(models.Model):
  firstname = models.CharField(max_length=30)
  lastname = models.CharField(max_length=30)

class Money_pot(models.Model):
  child = models.ForeignKey(Child, on_delete=models.CASCADE)
  balance = models.IntegerField()

class Task(models.Model):
  child = models.ForeignKey(Child, on_delete=models.CASCADE)
  date_created = models.DateField(auto_now_add=True)
  details = models.CharField(max_length=255)
  value = models.IntegerField()
  completed = models.BooleanField(default=False)