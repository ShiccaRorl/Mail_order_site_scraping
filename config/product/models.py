from django.db import models

# Create your models here.

# 商品
class Product(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    商品名 = models.TextField(verbose_name="商品名", default="")
    税抜き価格 = models.IntegerField(verbose_name="税抜き価格", default=0)
    消費税 = models.IntegerField(verbose_name="消費税", default=0)
    税率 = models.FloatField(verbose_name="税率", default=0.1)
    税入り価格 = models.IntegerField(verbose_name="税入り価格", default=0)
    QR_code = models.TextField(verbose_name="QR_code", default="")
    