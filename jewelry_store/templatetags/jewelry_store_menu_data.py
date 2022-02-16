from django import template
from jewelry_store.models import Category


register = template.Library()

@register.simple_tag

def menu_data():
    print('dupa')
    return {
        'categories': Category.objects.all()
    }