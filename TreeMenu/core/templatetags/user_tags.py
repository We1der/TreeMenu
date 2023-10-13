from django import template
from Menu.models import Menu, MenuItem
from django.shortcuts import get_object_or_404


register = template.Library()


@register.inclusion_tag('core/menu_items.html')
def draw_menu(parent):

    # checking parent is root item object or Menu object
    if type(parent) == MenuItem:
        menu_items = MenuItem.objects.filter(item_parent=parent).order_by(
            'position'
            )
        return {'menu_items': menu_items}

    menu = get_object_or_404(Menu, name=parent)
    # root menu items has item_parent = None
    menu_items = MenuItem.objects.filter(
        menu_parent=menu,
        item_parent=None,
    ).order_by('position')
    return {'menu_items': menu_items}
