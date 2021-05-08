from django.db import models

# Create your models here.

# 写真
class Photo(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    name = models.TextField(verbose_name="商品名", default="")
    商品_id