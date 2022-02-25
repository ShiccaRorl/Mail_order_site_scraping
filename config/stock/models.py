from django.db import models


# Create your models here.

class Stock(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    仕入れ日
    仕入れ
    仕入れ数量
    出荷日
    出荷
    出荷数量
    商品コード
    商品名
