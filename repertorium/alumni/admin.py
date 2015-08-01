from django.contrib import admin

from .models import Persoon, Rhetorica, Adres, Contact, Beroep
from .models import Klas, Klasfoto, Persoonfoto, Betaling, Betalingstype, Gebeurtenis, Hoedanigheid, Hoedanigheidstype, Contactmiddel

class AdresInline(admin.TabularInline):
	model = Adres
	extra = 0

class ContactInline(admin.TabularInline):
	model = Contact
	extra = 0

class BeroepInline(admin.TabularInline):
	model = Beroep
	extra = 0

class BetalingInline(admin.TabularInline):
	model = Betaling
	extra = 0
	
class GebeurtenisInline(admin.TabularInline):
	model = Gebeurtenis
	extra = 0

class PersoonfotoInline(admin.TabularInline):
	model = Persoonfoto
	extra = 0

class HoedanigheidInline(admin.TabularInline):
	model = Hoedanigheid
	extra = 0
		
class PersoonAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,
			{'fields': 
				['voornaam', 'achternaam', 'rhetorica', 
					'klasvertegenwoordiger']
			}
		),
		('Repertorium',
			{'fields':
				['user', 'oudid', 'publiek', 'contacteren', 'opmerkingen'],
				'classes': ['collapse']
			}
		),
		('Personalia', 
			{'fields': 
				['geslacht', 'overleden', 
					'geboortedatum', 'geboorteplaats', 
					'sterfdatum', 'sterfplaats'], 
				'classes': ['collapse']
			}
		),
	]
	inlines = [AdresInline,ContactInline,BeroepInline,GebeurtenisInline,PersoonfotoInline,HoedanigheidInline,BetalingInline]
	list_display = ('achternaam', 'voornaam', 'rhetorica', 'ouderdom', 'wijziging')
	list_display_links = ('voornaam', 'achternaam')
	list_filter = ['wijziging','betaling__betalingsjaar']
	search_fields = ['voornaam', 'achternaam', 'rhetorica__jaar', 'rhetorica__richting']
	
admin.site.register(Persoon, PersoonAdmin)

class RhetoricaInline(admin.TabularInline):
	model = Rhetorica
	extra = 0

class KlasfotoInline(admin.TabularInline):
	model = Klasfoto
	extra = 0
	
class KlasAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,
			{'fields':
				['jaar', 'klasnaam', 'titularis']
			}
		)
	]
	inlines = [RhetoricaInline, KlasfotoInline]
	search_fields = ['jaar', 'klasnaam', 'rhetorica__richting']
	
admin.site.register(Klas, KlasAdmin)

class BetalingstypeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,
			{'fields':
				['omschrijving', 'actief']
			}
		)
	]
	list_display = ('omschrijving','actief')
	
admin.site.register(Betalingstype, BetalingstypeAdmin)

class HoedanigheidstypeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,
			{'fields':
				['omschrijving', 'actief']
			}
		)
	]
	list_display = ('omschrijving','actief')
	
admin.site.register(Hoedanigheidstype, HoedanigheidstypeAdmin)

class ContactmiddelAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,
			{'fields':
				['naam', 'template', 'actief']
			}
		)
	]
	list_display = ('naam', 'template', 'actief')
	
admin.site.register(Contactmiddel, ContactmiddelAdmin)