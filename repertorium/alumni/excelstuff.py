import io
import xlsxwriter

from django.utils.translation import ugettext
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
        
        
    worksheet_s.merge_range('B2:E2',  u"{0} {1}".format(str(klas.jaar), klas.klasnaam), title)
    rij = 4

    if klas.titularis:
        worksheet_s.merge_range('B3:E3', u"{0}".format(klas.titularis), subtitle)
        rij = 5
    
    aantal_klassen = Rhetorica.objects.filter(klas=klas_id).count()
    
    if aantal_klassen>1:
        worksheet_s.write_string(rij, 5, 'Rhet.', header)
    
    worksheet_s.write_string(rij, 1, 'Naam', header)
    naambreedte = 3
    worksheet_s.write_string(rij, 2, 'Voornaam', header)
    voornaambreedte = 3
    worksheet_s.write_string(rij, 3, 'Adres', header)
    worksheet_s.write_string(rij, 4, 'E-mail', header)
    emailbreedte = 3
    
    for persoon in personen:
        rij = rij + 1
        
        if aantal_klassen>1:
            worksheet_s.write_string(rij, 5, persoon.rhetorica.richting, cell)
        
        if not persoon.overleden:
            worksheet_s.write_string(rij, 1, persoon.achternaam, cell)
            worksheet_s.write_string(rij, 2, persoon.voornaam, cell)
        
            adres = Adres.objects.filter(persoon_id=persoon.id).order_by('-van')[:1]
        
            if adres.count():
                for a in adres:
                    if a.geldig:
                        stijl = cell_adres
                    else:
                        stijl = cell_adres_ongeldig

                    worksheet_s.write_string(rij, 3, a.adres, stijl)
            
            email = Contact.objects.filter(persoon_id=persoon.id).filter(geldig=1).filter(contactmiddel__naam__exact='E-mail')[:1]
        
            if email.count():
                for e in email:
                    worksheet_s.write_string(rij, 4, e.contactdata, cell)
                    if len(e.contactdata)>emailbreedte: 
                        emailbreedte=len(e.contactdata)
       
        else:
            worksheet_s.write_string(rij, 1, "†"+persoon.achternaam, overleden)
            worksheet_s.write_string(rij, 2, persoon.voornaam, overleden)
           
        if len(persoon.achternaam)>naambreedte: 
            naambreedte=len(persoon.achternaam)
        if len(persoon.voornaam)>voornaambreedte: 
            voornaambreedte=len(persoon.voornaam)
        
        
    worksheet_s.set_column('B:B', naambreedte+2)
    worksheet_s.set_column('C:C', voornaambreedte+2)
    worksheet_s.set_column('D:D', 25)
    worksheet_s.set_column('E:E', emailbreedte+2)

    
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data