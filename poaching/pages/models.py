from django.db import models


class Camera(models.Model):
    camera_id = models.IntegerField()
    location = models.CharField(max_length=255, null= True, blank=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15)
    longitude =  models.DecimalField(max_digits=30, decimal_places=15)

    def __str__(self):
        return f'{self.latitude, self.longitude}'
# Create your models here.
# Camera Model
# camera id
# camera location
# latitude longitude
# map

# RAngers
# name
# latitude longitude
#phone no
#