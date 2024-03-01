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
    boss = models.ForeignKey('Director', on_delete=models.CASCADE, null=True )

class MainIngenire(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey('HeadAssistant', on_delete=models.CASCADE, null=True )

class SeniorMaster(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey('MainIngenire', on_delete=models.CASCADE, null=True )

class Master(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey('SeniorMaster', on_delete=models.CASCADE, null=True )

class Ingenire(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey('Master', on_delete=models.CASCADE, null=True )

class Miner(models.Model):
    fullName = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey('Ingenire', on_delete=models.CASCADE, null=True )