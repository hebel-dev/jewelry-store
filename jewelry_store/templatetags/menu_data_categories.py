from django import template

from jewelry_store.models import Collection

register = template.Library()

@register.simple_tag

def menu_data_categories():
    # print('dupa')
    return {
        'collections' : Collection.objects.all(),
    }