from django.contrib.auth.models import User
from django.db import models

from base.base_model import BaseModel


class Organization(BaseModel):
    slug = models.CharField(max_length=30, unique=True, verbose_name="識別子")
    name = models.CharField(max_length=50, verbose_name="組織名称")
    avatar = models.CharField(max_length=255, blank=True, null=True, verbose_name="ロゴ")
    website = models.URLField(blank=True, null=True, verbose_name="ウェブサイト")

    class Meta:
        db_table = 't_organization'
        verbose_name = '組織'
        verbose_name_plural = '組織一覧'


class OrganizationOwner(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="組織")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザー")

    class Meta:
        db_table = 't_organization_owner'
        ordering = ('created_dt',)
        default_permissions = ()
        verbose_name = '組織オーナー'
        verbose_name_plural = '組織オーナー一覧'


class OrganizationMember(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="組織")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザー")

    class Meta:
        db_table = 't_organization_member'
        ordering = ('created_dt',)
        default_permissions = ()
        verbose_name = '組織メンバー'
        verbose_name_plural = '組織メンバー一覧'


class OrganizationFollower(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="組織")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザー")

    class Meta:
        db_table = 't_organization_follower'
        ordering = ('created_dt',)
        default_permissions = ()
        verbose_name = '組織フォロワー'
        verbose_name_plural = '組織フォロワー一覧'
