from django import template
from app.models import Cat

register = template.Library()

def get_categories(context, order, count):
    #возвращаем список категорий с учётом полученных сортировок
    """Получение списка категорий"""
    categories = Cat.objects.filter(published=True).order_by(order)
    if count is not None:
        categories=categories[:count]
    return categories

@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def category_list(
        context, order='-name', count=None, template='base/blog/categories.html'):
    categories = get_categories(context, order, count)
    return {'template':template, 'category_list':categories}

@register.simple_tag(takes_context=True)
def for_category_list(context, count=None, order='-name'):
    """template tag выводит категории без своего шаблона"""
    return get_categories(context, order, count)
