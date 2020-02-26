from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
#from django.utils.translation import gettext_lazy as _
"""
схема позволяем указать что что-то нужно будет переводить, оно может измениться
from django.utils.translation import gerrext_lazy as _ 
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri"""


class Pages(models.Model):
    """Страницы"""
    title = models.CharField("Заголовок", max_length=500)
    sub_title = models.CharField("Подзаголовок", max_length=500, blank=True, null=True)
    text = models.TextField("Текст", blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    published = models.BooleanField("Опубликовать?", default=True)
    template = models.CharField("Шаблон", max_length=500, default="pages/home.html")
    registration_required = models.BooleanField(
        'Требуется регистрация',
        help_text="Если флажок установлен, только зарегистрированные пользователи могут "
                    "просматривать страницу.", # отобразится в админ панели рядом
        default=False,
    )
    slug = models.CharField("url", max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): #подставляем слеши для корректного построения url
        if self.slug is None: #если slug пуст, то делаем главную
            self.slug = "/"
        if not f"{self.slug}".startswith("/"): #если slug есть, то добавляем слеш в конец
            self.slug = "/" + self.slug
        if not self.slug.endswith("/"):
            self.slug += "/"
        super().save(*args, **kwargs)
        
    def get_absolute_url(self): #построение правильного url
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        unique_together = ('slug',)


