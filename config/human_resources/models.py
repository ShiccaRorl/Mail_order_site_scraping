from django.db import models


# Create your models here.

class T_人事(models.Model):
    日付 = models.DateField(default=None, blank=True, null=True)
    開始時間 = models.DateTimeField(auto_now=False, blank=True, null=True, default=None)
    終了時間 = models.DateTimeField(auto_now=False, blank=True, null=True, default=None)
    名前 = models.TextField(default="", blank=True, null=True)
    フリガナ = models.TextField(default="", blank=True, null=True)
    パスワード = models.TextField(default="", blank=True, null=True)
    ログイン状態 = models.BooleanField(default=False, blank=True, null=True)
    郵便番号 = models.TextField(default="", blank=True, null=True)
    住所 = models.TextField(default="", blank=True, null=True)
    連絡先 = models.TextField(default="", blank=True, null=True)
    在籍中 = models.BooleanField(default=False, blank=True, null=True)
    グループ1 = models.IntegerField(default=0, blank=True, null=True)
    グループ2 = models.IntegerField(default=0, blank=True, null=True)
    グループ3 = models.IntegerField(default=0, blank=True, null=True)
