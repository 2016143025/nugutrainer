from django.db import models
import random
# Create your models here.


class trainer(models.Model):
    gym = models.CharField(default='',max_length=20)
    name = models.CharField(default='',max_length=10)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    mapurl = models.TextField(default='')
    inform = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
class score(models.Model):
    trainer_id = models.OneToOneField(trainer,on_delete=models.CASCADE)
    score = models.IntegerField(default=8)
    def __str__(self):
        return str(self.score)
        
class gymlocation(models.Model):
    gym = models.TextField(default='')
    location = models.TextField(default='')
    
    def __str__(self):
        return self.gym
    
class RecordSearch(models.Model):
    searchtext = models.TextField(default='')
    
    def __str__(self):
        return str(self.id)