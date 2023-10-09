from django.contrib import admin
from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('description',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_parent', 'item_parent')
    empty_value_display = '0 - root'
    list_filter = ('menu_parent', 'item_parent', 'position')
    ordering = ('menu_parent', 'id', 'position', )


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
