from django.db import models

# Create your models here.

# 商品
class Product(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    name = models.TextField(verbose_name="商品名", default="")
    non_taxed_price = models.IntegerField(verbose_name="税抜き価格", default=0)
    consumption_tax = models.IntegerField(verbose_name="消費税", default=0)
    tax_rate = models.FloatField(verbose_name="税率", default=0.1)
    Price_including_tax = models.IntegerField(verbose_name="税入り価格", default=0)
    QR_code = models.TextField(verbose_name="QR_code", default="")
    