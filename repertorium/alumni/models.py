from datetime import datetime

from django.db import models
from django.utils import timezone

from sorl.thumbnail import ImageField

def ditjaar():
    return datetime.now().year
    
class Klas(models.Model):
    jaar = models.SmallIntegerField(default=ditjaar)
    klasnaam = models.CharField(max_length=50,null=True,blank=True)
    titularis = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        ret = str(self.jaar) + ' ' + self.klasnaam
        if self.titularis:    
            ret += ' (' + self.titularis + ')'
        return ret 
    class Meta:
        verbose_name_plural = 'Klassen'

class Rhetorica(models.Model):
    klas = models.ForeignKey(Klas,null=True,blank=True)
    jaar = models.SmallIntegerField(default=ditjaar)
    richting = models.CharField(max_length=16)
    def __str__(self):
        return str(self.jaar) + ' ' + self.richting
    class Meta:
        verbose_name_plural = 'Rhetorica\'s'
            
class Persoon(models.Model):
    voornaam = models.CharField(max_length=200,null=True,blank=True)
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
    
    oudid = models.IntegerField('tnr_oudleerling uit oude db', null=True,blank=True)
    klasvertegenwoordiger = models.BooleanField(default=False)
    publiek = models.BooleanField('mag online verschijnen?', default=True)
    contacteren = models.BooleanField('mag gecontacteerd worden?', default=True)
    opmerkingen = models.TextField(null=True,blank=True)
    
    wijziging = models.DateTimeField(auto_now=True)
    
    def leeftijd(self):
        if self.geboortedatum:
            if self.sterfdatum:
                return self.sterfdatum.year - self.geboortedatum.year - ((self.sterfdatum.month, self.sterfdatum.day) < (self.geboortedatum.month, self.geboortedatum.day))
            elif self.overleden:
                return '?'
            else:
                nu = datetime.now()
                return nu.year - self.geboortedatum.year - ((nu.month, nu.day) < (self.geboortedatum.month, self.geboortedatum.day))
        else:
            return ''
        
    def ouderdom(self):        
        if self.sterfdatum:
            temp = '†' + str(self.sterfdatum.year)
            if self.geboortedatum:
                return temp + ' (' + str(self.sterfdatum.year - self.geboortedatum.year - ((self.sterfdatum.month, self.sterfdatum.day) < (self.geboortedatum.month, self.geboortedatum.day))) + ' jaar)'
            elif self.rhetorica:
                return temp + ' (ca. ' + str(self.sterfdatum.year - self.rhetorica.jaar + 18) + ' jaar)'
            else:
                return ''
        elif self.overleden:
            return '†'
        elif self.geboortedatum:
            nu = datetime.now()
            temp = nu.year - self.geboortedatum.year - ((nu.month, nu.day) < (self.geboortedatum.month, self.geboortedatum.day))
            return str(temp) + ' jaar'
        elif self.rhetorica:
            return 'ca. ' + str(datetime.now().year - self.rhetorica.jaar + 18) + ' jaar'
        else:
            return ''
    
    def richting(self):
        if self.rhetorica:
            return self.rhetorica.richting
        else:
            return ''

    def __str__(self):
        if self.voornaam:
            return self.voornaam + ' ' + self.achternaam
        else:
            return self.achternaam
    
    class Meta:
        verbose_name_plural = 'Personen'

class Adres(models.Model):
    persoon = models.ForeignKey(Persoon)
    adres = models.TextField()
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    geldig = models.BooleanField(default=True)
    wijziging = models.DateTimeField(auto_now=True)
    def adreskomma(self):
        return self.adres.replace('\n',', ').replace(' ,',',').replace(',,',',')
    def __str__(self):
        return self.adres
    class Meta:
        verbose_name_plural = 'Adressen'

class Contactmiddel(models.Model):
    naam = models.CharField(max_length=50)
    template = models.CharField(max_length=200)
    actief = models.BooleanField(default=True)
    def __str__(self):
        return self.naam
    class Meta:
        verbose_name_plural = 'Contactmiddelen'

class Contact(models.Model):
    persoon = models.ForeignKey(Persoon)
    contactmiddel = models.ForeignKey(Contactmiddel)
    contactdata = models.CharField(max_length=200)
    opmerking = models.CharField(max_length=100,null=True,blank=True)
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    geldig = models.BooleanField(default=True)
    wijziging = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.contactmiddel.naam + ' ' + self.contactdata
    class Meta:
        verbose_name_plural = 'Contactmiddelen'

class Gebeurtenis(models.Model):
    persoon = models.ForeignKey(Persoon)
    GEBEURTENIS_GEBOORTE = 'geboorte'
    GEBEURTENIS_HUWELIJK = 'huwelijk'
    GEBEURTENIS_OVERLIJDEN = 'overlijden'
    GEBEURTENIS_OVERIGE = 'overige'
    GEBEURTENISTYPES = {(GEBEURTENIS_GEBOORTE, 'Geboorte'), (GEBEURTENIS_HUWELIJK, 'Huwelijk'), 
        (GEBEURTENIS_OVERLIJDEN, 'Overlijden'), (GEBEURTENIS_OVERIGE, 'Overige')}
    gebeurtenistype = models.CharField(max_length=10, choices=GEBEURTENISTYPES, default=GEBEURTENIS_GEBOORTE)
    datum = models.DateField(null=True,blank=True)
    omschrijving = models.TextField()
    wijziging = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.datum) + ' ' + self.omschrijving
    class Meta:
        verbose_name_plural = 'Gebeurtenissen'

class Beroep(models.Model):
    persoon = models.ForeignKey(Persoon)
    beroepsgegevens = models.CharField(max_length=500)
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    featured = models.BooleanField(default=False)
    wijziging = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.beroepsgegevens
    class Meta:
        verbose_name_plural = 'Beroepen'

class Klasfoto(models.Model):
    klas = models.ForeignKey(Klas)
    datum = models.DateField(null=True,blank=True)
    foto = models.ImageField(upload_to='klasfoto')
    legende = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Klasfoto\'s'

class Persoonfoto(models.Model):
    persoon = models.ForeignKey(Persoon)
    datum = models.DateField(null=True,blank=True)
    foto = models.ImageField(upload_to='klasfoto')
    legende = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Foto\'s'
 
class Betalingstype(models.Model):
    omschrijving = models.CharField(max_length=50)
    actief = models.BooleanField(default=True)
    def __str__(self):
        return self.omschrijving

class Betaling(models.Model):
    persoon = models.ForeignKey(Persoon)
    betalingstype = models.ForeignKey(Betalingstype)
    betalingsjaar = models.IntegerField(default=ditjaar, null=True,blank=True)
    bedrag = models.IntegerField(null=True,blank=True)
    opmerking = models.CharField(max_length=200,null=True,blank=True)
    datum = models.DateField(null=True,blank=True)
    class Meta:
        verbose_name_plural = "Betalingen"

class Hoedanigheidstype(models.Model):
    omschrijving = models.CharField(max_length=50)
    actief = models.BooleanField(default=True)
    def __str__(self):
        return self.omschrijving
    class Meta:
        verbose_name = "Hoedanigheid"
        verbose_name_plural = "Hoedanigheden"

class Hoedanigheid(models.Model):
    persoon = models.ForeignKey(Persoon)
    hoedanigheidstype = models.ForeignKey(Hoedanigheidstype)
    opmerking = models.CharField(max_length=100,null=True,blank=True)
    van = models.DateField(null=True,blank=True)
    tot = models.DateField(null=True,blank=True)
    geldig = models.BooleanField(default=True)
    wijziging = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.hoedanigheidstype.omschrijving
    class Meta:
        verbose_name_plural = 'Hoedanigheden'
  