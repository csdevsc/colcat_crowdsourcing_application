from django import template
from crowdsource.models import Task

register = template.Library()

@register.inclusion_tag('crowdsource/tasks.html')
def get_task_list(task=None):
    return {'tasks': Task.objects.all(), 'act_task': task}
