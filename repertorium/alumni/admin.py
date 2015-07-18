from django.contrib import admin

from .models import Persoon, Rhetorica, Adres, Contact, Beroep, Klas, Klasfoto

class AdresInline(admin.TabularInline):
	model = Adres
	extra = 0

class ContactInline(admin.TabularInline):
	model = Contact
	extra = 0

class BeroepInline(admin.TabularInline):
	model = Beroep
	extra = 0

class PersoonAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,
			{'fields': 
				['voornaam', 'achternaam', 'rhetorica', 
					'klasvertegenwoordiger','email']
			}
		),
		('Repertorium',
			{'fields':
				['oudid', 'publiek', 'contacteren', 'opmerkingen'],
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
	inlines = [AdresInline,ContactInline,BeroepInline]
	list_display = ('achternaam', 'voornaam', 'rhetorica', 'leeftijd', 'wijziging')
	list_display_links = ('voornaam', 'achternaam')
	list_filter = ['wijziging']
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
	search_fields = ['jaar', 'klasnaam', 'rhetorica__richting²']
	
	
admin.site.register(Klas, KlasAdmin)