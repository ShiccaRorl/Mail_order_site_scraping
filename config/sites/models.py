from django.db import models


# Create your models here.

class Site(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    name = models.TextField(verbose_name="サイト名", default="")
