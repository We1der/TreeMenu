from django.db import models


class Menu(models.Model):
    """ model for combining menu items """

    name = models.CharField('Menu name', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Menu'


class MenuItem(models.Model):
    """ presentation of menu items """

    name = models.CharField('Item name', max_length=100)
    url = models.URLField('Url', max_length=300)
    # Positions example:
    # [ Главная, Одежда, Техника] - example menu items
    #     1        2        3
    # Built-in menu items will also start from position 1:
    # [ 'Лето', 'Осень', 'Зима', 'Весна'] - items from 'Одежда'
    #     1        2       3        4
    position = models.PositiveIntegerField('Position', default=1)

    # Parent Menu model object
    menu_parent = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name='Menu',
    )

    # Parent menu item
    item_parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Item parent',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['menu_parent', 'position']
        verbose_name = 'Menu item'
