from django.db import models



class Position(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name

   
class Workers(models.Model):
    fullName = models.CharField(max_length=250)
    job_position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    position = models.ForeignKey('Position', on_delete=models.PROTECT)
    def __str__(self):
        return self.fullName


class Relations(models.Model):
    boss = models.ForeignKey('Workers', on_delete=models.CASCADE)
    worker = models.CharField(max_length=250)
 




