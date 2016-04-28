"""Models for managing tasks
"""

from django.db import models
import os

class Language(models.Model):
    class Meta:
        db_table = 'tbl_language_list'
    def __unicode__(self):
        return self.language_name
    language_id = models.CharField(primary_key=True, max_length=128, unique=True)
    language_name = models.CharField(max_length=128)

def image_directory_path(instance, filename):
    return os.path.join('data', instance.language_name.lower(), instance.task_type_name.lower(), filename)

class Image_Data(models.Model):
    """List of all images used in crowdsourcing tasks"""
    class Meta:
        db_table = 'tbl_image_data'
    def __unicode__(self):
        return str(self.image_filepath)
    image_id = models.AutoField(primary_key=True, max_length=128)
    language_name = models.CharField(max_length=128)
    task_type_name = models.CharField(max_length=128) # Foci, Naming, etc.
    image_filepath = models.FileField(upload_to=image_directory_path)

class Task_Type(models.Model):
    class Meta:
        db_table = 'tbl_task_types'
    def __unicode__(self):
        return self.task_type_name
    task_type_id = models.AutoField(primary_key=True, unique=True)
    task_type_name = models.CharField(max_length=128)
    task_template = models.CharField(max_length=128)
    data_model = models.CharField(max_length=64)

class Task_Template(models.Model):
    class Meta:
        db_table = 'tbl_task_templates'
    def __unicode__(self):
        return self.task_template_name
    task_template_id = models.AutoField(primary_key=True, unique=True)
    task_template_name = models.CharField(max_length=128)

class Data_Model(models.Model):
    class Meta:
        db_table = 'tbl_data_models'
    def __unicode__(self):
        return self.data_model
    data_model_id = models.AutoField(primary_key=True, unique=True)
    data_model = models.CharField(max_length=128) # FullGrid, FullGridConfidence, FullGridChecked

class Task(models.Model):
    class Meta:
        db_table = 'tbl_tasks'
    def __unicode__(self):
        return self.task_name
    task_id = models.AutoField(primary_key=True, unique=True)
    task_name = models.CharField(max_length=128)
    language_name = models.CharField(max_length=128)
    task_type_name = models.CharField(max_length=128)
    image_filepath = models.CharField(max_length=256)
    task_url = models.CharField(max_length=256)
