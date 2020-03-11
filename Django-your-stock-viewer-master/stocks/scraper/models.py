from django.db import models

# Create your models here.
class Stock(models.Model):
    
    code = models.CharField(max_length=20,null=False,blank="False")

    date = models.CharField(max_length=15,null=False,blank=False)

    def __str__(self):
        return self.code