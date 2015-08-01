import io
import xlsxwriter

from django.utils.translation import ugettext
from datetime import datetime

from .models import Klas, Persoon, Adres, Contact, Rhetorica

def XLSklaslijst(klas_id):
    
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Klaslijst")
    
    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 24,
        'align': 'left',
        'valign': 'vcenter'
    })
    subtitle = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'left',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#fafafa',
        'color': 'black',
        'align': 'left',
        'valign': 'top',
        'bottom': 1
    })
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
    })
    overleden = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'italic': True,
        'color': '#777777'
    })
    cell_adres = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True
    })
    cell_adres_ongeldig = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'color': '#cc0000'
    })
    
    klas = Klas.objects.get(pk=klas_id)
    personen = Persoon.objects.filter(rhetorica__klas=klas_id).order_by('rhetorica__richting', 'achternaam', 'voornaam')
    contacten = Contact.objects.filter(persoon__rhetorica__klas_id=klas_id).filter(persoon__overleden=0).filter(geldig=1).filter(contactmiddel__naam__exact="E-mail")
        
        
    worksheet_s.merge_range('A1:D1',  u"{0} {1}".format(str(klas.jaar), klas.klasnaam), title)
    rij = 3

    if klas.titularis:
        worksheet_s.merge_range('A2:D2', u"{0}".format(klas.titularis), subtitle)
        rij = 4
    
    aantal_klassen = Rhetorica.objects.filter(klas=klas_id).count()
    
    if aantal_klassen>1:
        worksheet_s.write_string(rij, 4, 'Rhet.', header)
    
    worksheet_s.write_string(rij, 0, 'Naam', header)
    naambreedte = 3
    worksheet_s.write_string(rij, 1, 'Voornaam', header)
    voornaambreedte = 3
    worksheet_s.write_string(rij, 2, 'Adres', header)
    worksheet_s.write_string(rij, 3, 'E-mail', header)
    emailbreedte = 3
    
    for persoon in personen:
        rij = rij + 1
        
        if aantal_klassen>1:
            worksheet_s.write_string(rij, 4, persoon.rhetorica.richting, cell)
        
        if not persoon.overleden:
            worksheet_s.write_string(rij, 0, persoon.achternaam, cell)
            worksheet_s.write_string(rij, 1, persoon.voornaam, cell)
        
            adres = Adres.objects.filter(persoon_id=persoon.id).order_by('-van')[:1]
        
            if adres.count():
                for a in adres:
                    if a.geldig:
                        stijl = cell_adres
                    else:
                        stijl = cell_adres_ongeldig

                    worksheet_s.write_string(rij, 2, a.adres, stijl)
            
            email = Contact.objects.filter(persoon_id=persoon.id).filter(geldig=1).filter(contactmiddel__naam__exact='E-mail')[:1]
        
            if email.count():
                for e in email:
                    worksheet_s.write_string(rij, 3, e.contactdata, cell)
                    if len(e.contactdata)>emailbreedte: 
                        emailbreedte=len(e.contactdata)
       
        else:
            worksheet_s.write_string(rij, 0, persoon.achternaam+"†", overleden)
            worksheet_s.write_string(rij, 1, persoon.voornaam, overleden)
           
        if len(persoon.achternaam)>naambreedte: 
            naambreedte=len(persoon.achternaam)
        if len(persoon.voornaam)>voornaambreedte: 
            voornaambreedte=len(persoon.voornaam)
        
        
    worksheet_s.set_column('A:A', naambreedte+2)
    worksheet_s.set_column('B:B', voornaambreedte+2)
    worksheet_s.set_column('C:C', 35)
    worksheet_s.set_column('D:D', emailbreedte+2)

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data

def XLSadreslijst(context):
    
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Adreslijst")
    
    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 24,
        'align': 'left',
        'valign': 'vcenter'
    })
    subtitle = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'left',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#fafafa',
        'color': 'black',
        'align': 'left',
        'valign': 'top',
        'bottom': 1
    })
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
    })
    cell_adres = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True
    })
        
    personen = context['personen']
    titel = context['titel']
    
    worksheet_s.merge_range('A1:F1', u"{0}".format(titel), title)
    worksheet_s.merge_range('A2:F2', u"Adreslijst aangemaakt op {0}".format(datetime.now().strftime('%d/%m/%Y')) , subtitle)
    
    worksheet_s.write_string(4, 0, 'Naam', header)
    naambreedte = 3
    worksheet_s.write_string(4, 1, 'Voornaam', header)
    voornaambreedte = 3
    worksheet_s.write_string(4, 2, 'Rhet.', header)
    rhetbreedte = 3
    worksheet_s.write_string(4, 3, 'Adres', header)
    worksheet_s.write_string(4, 4, 'E-mail', header)
    emailbreedte = 3
    
    teller = 0
    for persoon in personen:
        teller = teller + 1
        
        if persoon.achternaam:
            worksheet_s.write_string(teller+4, 0, persoon.achternaam, cell)
            if len(persoon.achternaam)>naambreedte: 
                naambreedte=len(persoon.achternaam)
                
        if persoon.voornaam:
            worksheet_s.write_string(teller+4, 1, persoon.voornaam, cell)
            if len(persoon.voornaam)>voornaambreedte: 
                voornaambreedte=len(persoon.voornaam)
                
        if persoon.jaar:
            rhet = str(persoon.jaar) + " " + persoon.richting
        else:
            rhet = persoon.richting
        worksheet_s.write_string(teller+4, 2, rhet, cell)
        if len(rhet)>rhetbreedte: 
                rhetbreedte=len(rhet)
                
        worksheet_s.write_string(teller+4, 3, persoon.adres, cell_adres)
        
        if persoon.email:
            worksheet_s.write_string(teller+4, 4, persoon.email, cell)
            if len(persoon.email)>emailbreedte:
                emailbreedte=len(persoon.email)            
        
    worksheet_s.set_column('A:A', naambreedte+2)
    worksheet_s.set_column('B:B', voornaambreedte+2)
    worksheet_s.set_column('C:C', rhetbreedte+2)
    worksheet_s.set_column('D:D', 35)
    worksheet_s.set_column('E:E', emailbreedte+2)
    
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data