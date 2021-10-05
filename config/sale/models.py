from django.db import models

# Create your models here.

# 販売
class Sele(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    
    日付 = models.DateTimeField(verbose_name="日付", auto_now_add=True)
    商品コード = models.TextField(verbose_name="商品コード", default="")
    商品名 = models.TextField(verbose_name="商品名", default="")
    数量 = models.IntegerField(verbose_name="数量", default=1)
    消費税 = models.IntegerField(verbose_name="消費税", default=0)
    売価 = models.IntegerField(verbose_name="売価", default=0)
    販売サイト_code = models.IntegerField(verbose_name="販売サイト_code", default=0)
    販売サイト = models.TextField(default="")
    購入者_code = models.IntegerField(verbose_name="購入者_code", default=0)
    購入者 = models.TextField(default="")
    送り先_code = models.IntegerField(verbose_name="送り先_code", default=0)
    送り先 = models.TextField(default="")
    

class Sale_Product(models.Model):
    販売コード = models.TextField(verbose_name="code", default="")
    商品コード = models.TextField(verbose_name="商品コード", default="")

