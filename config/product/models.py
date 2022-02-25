from django.db import models


# Create your models here.

# 商品
class Product(models.Model):
    code = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    商品名 = models.TextField(default="", null=True, blank=True)
    下代 = models.IntegerField(default=0, null=True, blank=True)
    税抜き価格 = models.IntegerField(verbose_name="税抜き価格", default=0, null=True, blank=True)
    消費税 = models.IntegerField(verbose_name="消費税", default=0, null=True, blank=True)
    税率 = models.FloatField(verbose_name="税率", default=0.1, null=True, blank=True)
    税入り価格 = models.IntegerField(verbose_name="税入り価格", default=0, null=True, blank=True)
    QR_code = models.TextField(default="", null=True, blank=True)
    配送方法 = models.TextField(default="", null=True, blank=True)
