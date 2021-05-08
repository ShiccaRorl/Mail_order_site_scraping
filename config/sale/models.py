from django.db import models

# Create your models here.

# 販売
class Sele(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    日付
    商品コード
    name = models.TextField(verbose_name="商品名", default="")
    数量
    消費税
    売価
    販売サイト_id
    購入者_id
    送り先_id
    