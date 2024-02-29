from django.db import models


class Director(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()

class HeadAssistant(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss_id = models.ForeignKey('Director', on_delete=models.CASCADE )

class MainIngenire(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss_id = models.ForeignKey('HeadAssistant', on_delete=models.CASCADE )

class SeniorMaster(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss_id = models.ForeignKey('MainIngenire', on_delete=models.CASCADE )

class Master(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss_id = models.ForeignKey('SeniorMaster', on_delete=models.CASCADE )

class Ingenire(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss_id = models.ForeignKey('Master', on_delete=models.CASCADE )

class Miner(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss_id = models.ForeignKey('Ingenire', on_delete=models.CASCADE )