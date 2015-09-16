"""Models for tasks

Each new type of task corresponds to a task model
"""

from django.db import models
from data import Data_FullGrid_Confidence, Data_FullGrid

# Tasks
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
    dt_completed = models.DateTimeField(auto_now=True)

class Task_Mapping_001(Data_FullGrid):
    class Meta:
        db_table = 'tbl_response_mapping_001'
    def __unicode__(self):
        return 'Task Mapping 001'
    task_response_id = models.AutoField(primary_key=True, unique=True)
    worker_id = models.CharField(max_length=128)
    task_response_key = models.CharField(max_length=32, unique=True)
