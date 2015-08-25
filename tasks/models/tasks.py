"""Models for tasks

Each new type of task corresponds to a task model
"""

from django.db import models
from data import Data_FullGrid_Confidence, Data_FullGrid

class Task_Prescreen_01(models.Model):
    class Meta:
        db_table = 'tbl_response_prescreen'
    def __unicode__(self):
        return 'Prescreen task'
    task_response_id = models.AutoField(primary_key=True, unique=True)
    worker_id = models.CharField(max_length=128)
    task_response_key = models.CharField(max_length=32, unique=True)

    answer_01 = models.CharField(max_length=16)
    answer_02 = models.CharField(max_length=16)
    answer_03 = models.CharField(max_length=16)
    answer_04 = models.CharField(max_length=16)
    answer_05 = models.CharField(max_length=16)
    answer_06 = models.CharField(max_length=16)
    answer_07 = models.CharField(max_length=16)
    answer_08 = models.CharField(max_length=16)
    answer_09 = models.CharField(max_length=16)
    answer_10 = models.CharField(max_length=16)
    answer_11 = models.CharField(max_length=16)
    answer_12 = models.CharField(max_length=16)
    answer_13 = models.CharField(max_length=16)
    answer_14 = models.CharField(max_length=16)
    answer_15 = models.CharField(max_length=16)
    answer_16 = models.CharField(max_length=16)
    answer_17 = models.CharField(max_length=16)
    answer_18 = models.CharField(max_length=16)
    answer_19 = models.CharField(max_length=16)
    answer_20 = models.CharField(max_length=16)

class Task_Naming_001(Data_FullGrid_Confidence):
    class Meta:
        db_table = 'tbl_response_naming_001'
    def __unicode__(self):
        return 'Task Naming 001'
    task_response_id = models.AutoField(primary_key=True, unique=True)
    worker_id = models.CharField(max_length=128)
    task_response_key = models.CharField(max_length=32, unique=True)

class Task_Foci_001(Data_FullGrid):
    class Meta:
        db_table = 'tbl_response_foci_001'
    def __unicode__(self):
        return 'Task Foci 001'
    task_response_id = models.AutoField(primary_key=True, unique=True)
    worker_id = models.CharField(max_length=128)
    task_response_key = models.CharField(max_length=32, unique=True)

class Task_Mapping_001(Data_FullGrid):
    class Meta:
        db_table = 'tbl_response_mapping_001'
    def __unicode__(self):
        return 'Task Mapping 001'
    task_response_id = models.AutoField(primary_key=True, unique=True)
    worker_id = models.CharField(max_length=128)
    task_response_key = models.CharField(max_length=32, unique=True)
