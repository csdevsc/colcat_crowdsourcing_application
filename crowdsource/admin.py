from django.contrib import admin
from crowdsource.models import Task, Response

class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('task_id', 'name', 'responses', 'task_type')

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'submitted_by', 'task')

admin.site.register(Task, TaskAdmin)
admin.site.register(Response, ResponseAdmin)
