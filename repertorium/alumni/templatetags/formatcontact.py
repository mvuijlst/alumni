import re 

from django import template
register = template.Library()

@register.filter
def formatcontact ( string, args ): 
        
    return re.sub( '£', args, string )
