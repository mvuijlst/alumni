from django.db import models

class Persoon(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)
    geboortedatum = models.DateField(null=True)
    sterfdatum = models.DateField(null=True)
    email = models.EmailField(null=True)
    oudid = models.IntegerField('tnr_oudleerling uit oude db', null=True)

class Adres(models.Model):
    persoon = models.ForeignKey(Persoon)
    adres = models.TextField()
    van = models.DateField(null=True)
    tot = models.DateField(null=True)
    geldig = models.BooleanField(default=True)
