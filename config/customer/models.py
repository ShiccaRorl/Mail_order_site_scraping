from django.db import models

# Create your models here.

# 客
class Product(models.Model):
    code = models.TextField(verbose_name="code")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
    name = models.TextField(verbose_name="商品名", default="")
    pen_name = models.TextField(verbose_name="ペンネーム", default="")
    zip_code = models.TextField(verbose_name="郵便番号", default="")
    address = models.TextField(verbose_name="住所", default="")
    phone_number = models.TextField(verbose_name="電話番号", default="")
    email_address = models.TextField(verbose_name="メールアドレス", default="")