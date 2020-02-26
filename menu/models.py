from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
#from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(models.Model):
    """Позиция меню"""
    name = models.CharField("Название", max_length=255)
    status = models.BooleanField("Только для зарегистрированных", default=False)
    published = models.BooleanField("Отображать?", default=True)

    def __str__(self): #получаем имя класса
        return self.name

    def items(self): #получаем все элементы меню
        return self.menuitem_set.all()

    class Meta:
        verbose_name = "Меню" #перевод
        verbose_name_plural = "Меню"


class MenuItem(MPTTModel): # через mptt для реализации вложенности меню
    """Элементы меню"""
    title = models.CharField("Название пункта меню на сайте", max_length=255)
    name = models.CharField("Название латиницей", max_length=255)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительский пункт",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name="Меню", on_delete=models.CASCADE)
    status = models.BooleanField("Только для зарегистрированных", default=False)

    url = models.CharField("url на внешний ресурс", max_length=255, null=True, blank=True)
    anchor = models.CharField("Якорь", max_length=255, null=True, blank=True)

    content_type = models.ForeignKey(
        ContentType, #завязываемся на таблице для возможности связать поля с любым приложением\моделью
        verbose_name="Ссылка на",
        #limit_choices_to=settings.MENU_APPS, сколько и чего отображать
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    object_id = models.PositiveIntegerField(verbose_name='Id записи', default=1, null=True)# id записи для связки
    content_object = GenericForeignKey('content_type', 'object_id')# связываем cont type и obj_id
    sort = models.PositiveIntegerField('Порядок', default=0)
    published = models.BooleanField("Отображать?", default=True)

    def get_anchor(self): #возвращает корректную ссылку если есть якорь
        if self.anchor:
            return "{}/#{}".format(Site.objects.get_current().domain, self.anchor) #Site.objects возвращает ссылку на текущий сайт
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_description = 'ID'

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    class MPTTMeta:
        order_insertion_by = ('sort',)

