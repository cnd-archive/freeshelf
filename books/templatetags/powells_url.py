from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def powells_url(isbn):
    partner_id = settings.POWELLS_ID
    url = "http://www.powells.com/partner/%s/biblio/%s?p_isbn" % (partner_id, isbn)
    return url
