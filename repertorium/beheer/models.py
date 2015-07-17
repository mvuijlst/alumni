from django.utils import timezone
from django.db import models

class Rhetorica(models.Model):
    jaar = models.SmallIntegerField()
    richting = models.CharField(max_length=16)
    titularis = models.CharField(max_length=200)
    def __str__(self):
        return str(self.jaar) + ' ' + self.richting + ' (' + self.titularis + ')'
    
class Persoon(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)
    rhetorica = models.ForeignKey(Rhetorica,null=True,blank=True)
    geboortedatum = models.DateField(null=True,blank=True)
    sterfdatum = models.DateField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    oudid = models.IntegerField('tnr_oudleerling uit oude db', null=True,blank=True)
    wijziging = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.voornaam + ' ' + self.achternaam

class Adres(models.Model):
    persoon = models.ForeignKey(Persoon)
    adres = models.TextField()
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    geldig = models.BooleanField(default=True)
    wijziging = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.adres

