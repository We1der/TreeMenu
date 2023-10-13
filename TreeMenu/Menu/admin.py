from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    ordering = ('item_parent', 'position')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # MenuItems will display at Menu admin page
    inlines = [MenuItemInline]


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_parent', 'item_parent')
    empty_value_display = 'root'
    list_filter = ('menu_parent', 'item_parent', 'position')
    ordering = ('menu_parent', 'position', )
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
