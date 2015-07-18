from django.contrib import admin

from .models import Persoon, Rhetorica, Adres, Contact

class AdresInline(admin.TabularInline):
	model = Adres
	extra = 0

class ContactInline(admin.TabularInline):
	model = Contact
	extra = 0

class PersoonAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,         {'fields': ['voornaam', 'achternaam', 'rhetorica', 'email', 'oudid']}),
		('Personalia', 
			{'fields': 
				['geslacht', 'overleden', 
					'geboortedatum', 'geboorteplaats', 
					'sterfdatum', 'sterfplaats'], 
				'classes': ['collapse']
			}
		),
	]
	inlines = [AdresInline,ContactInline]
	list_display = ('voornaam', 'achternaam', 'rhetorica', 'leeftijd', 'wijziging')
	list_filter = ['wijziging']
	search_fields = ['voornaam', 'achternaam']
	
admin.site.register(Persoon, PersoonAdmin)

admin.site.register(Rhetorica)