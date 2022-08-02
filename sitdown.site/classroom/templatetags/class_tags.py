from django import template

from classroom.models import Classroom

register = template.Library()


@register.simple_tag()
def get_classroom():
    return Classroom.objects.all()
