from django.db import models

# Create your models here.
# 出品サポート
class product_listing_assistance():
    product_listing_assistance_cood = models.IntegerField(default=0, primary_key=True)
    商品コード = models.TextField(verbose_name="code", default="", blank=True, null=True)
    下代 = models.IntegerField(default=0, blank=True, null=True)
    売価 = models.IntegerField(default=0, blank=True, null=True)
    消費税 = models.IntegerField(default=0, blank=True, null=True)
    税込み価格 = models.IntegerField(default=0, blank=True, null=True)
    タイトル = models.TextField(default="", blank=True, null=True)
    バリエーション有り = models.BooleanField(default=False, blank=True, null=True)
    柄有り = models.BooleanField(default=False, blank=True, null=True)
    登録日 = models.DateTimeField(auto_now=True, blank=True, null=True)
    更新日 = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class Amazon(product_listing_assistance):
    cood = models.TextField(verbose_name="code", default="", blank=True, null=True)
    タイトル = models.TextField(verbose_name="code", default="", blank=True, null=True)
    売価 = models.IntegerField(default=0, blank=True, null=True)

class Rakuten(product_listing_assistance):
    cood = models.TextField(verbose_name="code", default="", blank=True, null=True)
    タイトル = models.TextField(verbose_name="code", default="", blank=True, null=True)
    売価 = models.IntegerField(default=0, blank=True, null=True)
