from django.db import models

# Create your models here.

# 写真
class Photo(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    file_name = models.TextField(verbose_name="ファイル名", default="")
    product_code = models.ForeignKey(Product, verbose_name="商品_code", default="")