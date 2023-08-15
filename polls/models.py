from django.db import models
from datetime import datetime


# Create your models here.

class YangilikModels(models.Model):
    Y_nomi = models.CharField(default='', max_length=150)
    Y_turi = models.CharField(default='', max_length=150)
    Y_matni = models.CharField(max_length=1300, default='')
    Y_vaxti = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.Y_nomi

    class Meta:
        db_table = 'yangilik'




# Create your models here.
