from django.db import models

# Create your models he:re.
class Data(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    mobile = models.IntegerField()
    mail = models.CharField(max_length=50)