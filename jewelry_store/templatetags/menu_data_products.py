from django import template
from jewelry_store.models import Category, Collection


register = template.Library()

@register.simple_tag

def menu_data_products():
    # print('dupa')
    return {
        'categories': Category.objects.all(),
    }
