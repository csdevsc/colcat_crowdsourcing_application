from django import template
from crowdsourcing.models import Task

register = template.Library()

@register.inclusion_tag('crowdsourcing/tasks.html')
def get_task_list(task=None):
    return {'tasks': Task.objects.all(), 'act_task': task}
