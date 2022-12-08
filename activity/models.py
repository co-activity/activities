from django.contrib.auth.models import User
from django.db import models

from base.base_model import BaseModel
from org.models import Organization
from utils import constants


class ActivityCategory(BaseModel):
    code = models.CharField(max_length=8, primary_key=True, verbose_name="カテゴリーコード")
    name = models.CharField(max_length=10, verbose_name="カテゴリー名称")
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, blank=True, null=True, verbose_name="組織")

    class Meta:
        db_table = 't_activity_category'
        unique_together = ('name', 'organization')
        ordering = ('code',)
        default_permissions = ()
        verbose_name = '組織オーナー'
        verbose_name_plural = '組織オーナー一覧'


class Activity(BaseModel):
    name = models.CharField(max_length=100, verbose_name="活動名称")
    content = models.TextField(max_length=5000, verbose_name="活動内容")
    start_date = models.DateField(blank=True, null=True, verbose_name="開始日")
    end_date = models.DateField(blank=True, null=True, verbose_name="終了日")
    category = models.ForeignKey(ActivityCategory, models.PROTECT, verbose_name="活動カテゴリー")
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, blank=True, null=True, verbose_name="組織")
    flg_privacy = models.CharField(
        max_length=1, default='0', choices=constants.CHOICE_FLG_PRIVACY, verbose_name="プライバシー区分"
    )
    created_user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='created_activity_set', verbose_name="作成者"
    )
    updated_user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='updated_activity_set', verbose_name="更新者"
    )
