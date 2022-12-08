from django.db import models


class BaseModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_dt = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    deleted_dt = models.DateTimeField(blank=True, null=True, verbose_name="削除日時")

    class Meta:
        abstract = True
