from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Seeds(models.Model):
    id = models.AutoField(default=0)
    seeds = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)