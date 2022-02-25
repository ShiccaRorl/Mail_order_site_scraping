from django.db import models


# Create your models here.
class generator(models.Model):
    __tablename__ = 'generator'

    # id = models.IntegerField(default=0, primary_key=True)
    ソース = models.TextField(default="", blank=True, null=True)
    商品コード = models.TextField(default="", blank=True, null=True)
    商品名 = models.TextField(default="", blank=True, null=True)
    税抜き価格 = models.IntegerField(default=0, blank=True, null=True)
    税込み価格 = models.IntegerField(default=0, blank=True, null=True)
    ラクマ価格 = models.IntegerField(default=0, blank=True, null=True)
    税率 = models.FloatField(verbose_name="税率", default=0.1, null=True, blank=True)

    発送方法_ストアクリエイター = models.TextField(default="", blank=True, null=True)
    発送方法_アマゾン = models.TextField(default="", blank=True, null=True)
    発送方法_楽天 = models.TextField(default="", blank=True, null=True)
    発送方法_ヤフオク = models.TextField(default="", blank=True, null=True)
    発送方法_ラクマ = models.TextField(default="", blank=True, null=True)

    商品説明_サイズ = models.TextField(default="", blank=True, null=True)
    商品説明_品質 = models.TextField(default="", blank=True, null=True)
    商品説明_生産国 = models.TextField(default="", blank=True, null=True)


class config(models.Model):
    柄 = models.TextField(default="", blank=True, null=True)
    バリエーション = models.TextField(default="", blank=True, null=True)
