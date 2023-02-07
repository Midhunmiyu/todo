from django.db import models

# Create your models here.
class todo(models.Model):
    reminder= models.CharField(max_length=100)
    date= models.DateField()

    def __str__(self):
        return self.reminder
