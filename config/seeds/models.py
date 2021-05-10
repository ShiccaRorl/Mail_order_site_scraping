from django.db import models

# Create your models here.

class Seeds(models.Model):
    site_code = models.IntegerField(verbose_name="販売サイト_code", default=0)
    seeds = models.TextField(verbose_name="ソースデータ", default="")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)