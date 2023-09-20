from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Child(models.Model):
  firstname = models.CharField(max_length=30)
  lastname = models.CharField(max_length=30)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Money_pot(models.Model):
  child = models.ForeignKey(Child, on_delete=models.CASCADE)
  balance = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP')
  def __str__(self):
    return f"{self.child.firstname} {self.child.lastname}'s moneypot"

class Task(models.Model):
  child = models.ForeignKey(Child, on_delete=models.CASCADE)
  date_created = models.DateField(auto_now_add=True)
  title = models.CharField(max_length=50)
  details = models.CharField(max_length=255)
  value = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP')
  completed = models.BooleanField(default=False)
  def __str__(self):
    return f"{self.title} - {self.child.firstname}"