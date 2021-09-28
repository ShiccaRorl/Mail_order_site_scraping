from django.db import models

# Create your models here.

class Seeds(models.Model):
    __tablename__ = 'T_Seeds'
    
    site_code = models.IntegerField(verbose_name="販売サイト_code", default=0, blank=True, null=True)
    seeds = models.TextField(verbose_name="ソースデータ", default="", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True, blank=True, null=True)
    
class T_販売サイト(models.Model):
    __tablename__ = 'T_販売サイト'
    
    site_code = models.IntegerField(verbose_name="販売サイト_code", default=0, blank=True, null=True)
    名前 = models.TextField(verbose_name="名前", default="", blank=True, null=True)
    url = models.TextField(verbose_name="リンク", default="", blank=True, null=True)
    user = models.TextField(verbose_name="ユーザー", default="", blank=True, null=True)
    password = models.TextField(verbose_name="パスワード", default="", blank=True, null=True)
    memo = models.TextField(verbose_name="メモ", default="", blank=True, null=True)