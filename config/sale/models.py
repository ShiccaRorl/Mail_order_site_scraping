from django.db import models

# Create your models here.

# 販売
class Sele(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    date_time = models.DateTimeField(verbose_name="日付", auto_now_add=True)
    product_code = models.TextField(verbose_name="商品コード", default="")
    name = models.TextField(verbose_name="商品名", default="")
    quantity = models.IntegerField(verbose_name="数量", default=1)
    consumption_tax = models.IntegerField(verbose_name="消費税", default=0)
    selling_price = models.IntegerField(verbose_name="売価", default=0)
    site_code = models.ForeignKey(Site, verbose_name="販売サイト_code", default=0)
    purchase_code = models.ForeignKey(Product, verbose_name="購入者_code", default=0)
    destination_code = models.ForeignKey(Product, verbose_name="送り先_code", default=0)
    