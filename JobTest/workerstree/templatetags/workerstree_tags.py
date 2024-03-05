from django import template
import workerstree.views as views
from workerstree.models import Position

register = template.Library()


@register.inclusion_tag('workerstree/center/center_left.html')
def position(cat_selected=0):
    cats = Position.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}