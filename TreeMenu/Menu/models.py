from django.db import models


class Menu(models.Model):
    """ model for combining menu items """

    description = models.CharField('Menu description', max_length=250)

    def __str__(self):
        return f'Menu: {self.description[:15]}'

    class Meta:
        ordering = ['description']
        verbose_name = 'Menu'


class MenuItem(models.Model):
    """ presentation of menu items """

    name = models.CharField('Title', max_length=100)
    url = models.URLField('Url', max_length=300)
    position = models.PositiveIntegerField('Position', default=1)
    menu_parent = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name='Menu',
    )
    item_parent = models.ForeignKey(
        'MenuItem',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Item parent',
    )

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        ordering = ['menu_parent', 'position']
        verbose_name = 'Menu item'
