from django import forms
from django.forms import ModelForm
from tasks.models import Task_Foci_001
from manage.models import *

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ('language_id', 'language_name',)

class ImageForm(ModelForm):
    class Meta:
        model = Image_Data
        fields = ('language_name', 'task_type_id', 'image_filepath')
    language_name = forms.ModelChoiceField(queryset=Language.objects.all().order_by('language_name'), to_field_name="language_name")
    task_type_id = forms.ModelChoiceField(queryset=Task_Type.objects.all().order_by('task_type_id'))

class DataModelForm(ModelForm):
    class Meta:
        model = Data_Model
        fields = ('data_model',)

class TaskTypeForm(ModelForm):
    class Meta:
        model = Task_Type
        fields = ('task_type_name', 'task_template', 'data_model')
    task_template = forms.ModelChoiceField(queryset=Task_Template.objects.all().order_by('task_template_id'))
    data_model = forms.ModelChoiceField(queryset=Data_Model.objects.all().order_by('data_model_id'))

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('language_id', 'task_type_id', 'image_id', 'from_mturk')
    language_id = forms.ModelChoiceField(queryset=Language.objects.all().order_by('language_name'), to_field_name="language_id")
    task_type_id = forms.ModelChoiceField(queryset=Task_Type.objects.all().order_by('task_type_name'))
    image_id = forms.ModelChoiceField(queryset=Image_Data.objects.all().order_by('image_id'), to_field_name="image_id")
    from_mturk = forms.BooleanField(required=False)

class TaskTemplateForm(ModelForm):
    class Meta:
        model = Task_Template
        fields = ('task_template_name', 'task_template_description', 'task_template_html')

class BatchForm(forms.Form):
    choices = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
    )
