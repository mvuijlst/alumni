import datetime

from django.db import models
from django.utils import timezone

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
    
    # geslachten
    GESLACHT_MAN = 'M'
    GESLACHT_VROUW = 'V'
    GESLACHT_ANDER = 'A'
    GESLACHT_ONBEKEND = '?'
    GESLACHTEN = {(GESLACHT_MAN, 'man'), (GESLACHT_VROUW, 'vrouw'), (GESLACHT_ANDER, 'ander'), (GESLACHT_ONBEKEND, 'onbekend')}
    geslacht = models.CharField(max_length=1, choices=GESLACHTEN, default=GESLACHT_MAN)    
    #overige personalia
    overleden = models.BooleanField(default=False)
    geboortedatum = models.DateField(null=True,blank=True)
    geboorteplaats = models.CharField(max_length=200,null=True,blank=True)
    sterfdatum = models.DateField(null=True,blank=True)
    sterfplaats = models.CharField(max_length=200,null=True,blank=True)
    
    email = models.EmailField(null=True,blank=True)
    oudid = models.IntegerField('tnr_oudleerling uit oude db', null=True,blank=True)
    wijziging = models.DateTimeField(auto_now=True)
    def leeftijd(self):
        nu = datetime.date.today()
        return nu.year - self.geboortedatum.year - ((nu.month, nu.day) < (self.geboortedatum.month, self.geboortedatum.day))
    def __str__(self):
        return self.voornaam + ' ' + self.achternaam

class Adres(models.Model):
    persoon = models.ForeignKey(Persoon)
    adres = models.TextField()
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    geldig = models.BooleanField(default=True)
    wijziging = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.adres

