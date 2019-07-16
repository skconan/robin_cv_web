from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(primary_key=True,max_length=50)
    is_label = models.BooleanField(default=False)
    mission_1 = models.CharField(max_length=20)
    mission_2 = models.CharField(max_length=20)
    mission_3 = models.CharField(max_length=20)
    mission_4 = models.CharField(max_length=20)
    mission_5 = models.CharField(max_length=20)
    mission_6 = models.CharField(max_length=20)
    mission_7 = models.CharField(max_length=20)
    mission_8 = models.CharField(max_length=20)    
    def __str__(self):
        return self.name
