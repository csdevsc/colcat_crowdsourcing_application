from django.db import models
from django.template.defaultfilters import slugify

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    instructions = models.TextField()
    responses = models.IntegerField(default=0)
    TASK_TYPE_CHOICES = (
        ('T', 'Transcription'),
        ('V', 'Verification'),
    )
    task_type = models.CharField(max_length=1,
                                 choices=TASK_TYPE_CHOICES,
                                 default='T')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Response(models.Model):
    response_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task)
    submitted_by = models.CharField(max_length=128)   # models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.task) + " - Response #" + str(self.response_id)

# For piloting purposes
# class Survey(models.Model):
#     survey_id = models.AutoField(primary_key=True)
#     submitted_by = models.CharField(max_length=128)
