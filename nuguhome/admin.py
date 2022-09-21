from django.contrib import admin

# Register your models here.
from .models import gymlocation, trainer, score
@admin.register(trainer)
class trainerAdmin(admin.ModelAdmin):
    list_display= ['id','gym','name','created_at']
    search_fields = ['name']
    list_filter = ['created_at']
#admin.site.register(trainer)
admin.site.register(score)
admin.site.register(gymlocation)