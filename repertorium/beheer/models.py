from django.utils import timezone
from django.db import models

class Persoon(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)
    geboortedatum = models.DateField(null=True,blank=True)
    sterfdatum = models.DateField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    oudid = models.IntegerField('tnr_oudleerling uit oude db', null=True,blank=True)
    wijzigdatum = models.DateField(default=timezone.now)
    def __str__(self):
        return self.voornaam + ' ' + self.achternaam

class Adres(models.Model):
    persoon = models.ForeignKey(Persoon)
    adres = models.TextField()
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    geldig = models.BooleanField(default=True)
    wijzigdatum = models.DateField(default=timezone.now)
    def __str__(self):
        return self.adres
