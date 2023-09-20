from django.contrib import admin
from .models import Child, Money_pot, Task

# Register your models here.

admin.site.register(Child)
admin.site.register(Money_pot)
admin.site.register(Task)