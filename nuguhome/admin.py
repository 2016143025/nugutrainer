from django.contrib import admin

# Register your models here.
from .models import gymlocation, trainer

admin.site.register(trainer)
#admin.site.register(score)
admin.site.register(gymlocation)