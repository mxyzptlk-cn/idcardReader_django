from django.db import models


class Visitors(models.Model):
    visitor = models.CharField(max_length=6, null=True, blank=True, verbose_name='姓名')
    gender = models.BooleanField(null=True, blank=True, verbose_name='性别')
    id_no = models.CharField(max_length=18, null=True, blank=True, verbose_name='身份证号')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='住址')
    phone = models.CharField(max_length=13, null=True, blank=True, verbose_name='联系电话')
    temp = models.FloatField(verbose_name='体温')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='登记时间')
    visitee = models.CharField(max_length=6, null=True, blank=True, verbose_name='探视患者')
    bk1 = models.CharField(max_length=6, null=True, blank=True, verbose_name='bk1')
    bk2 = models.CharField(max_length=8, null=True, blank=True, verbose_name='bk2')
    bk3 = models.CharField(max_length=8, null=True, blank=True, verbose_name='bk3')
    
    valid = models.BooleanField(default=True, verbose_name='记录状态')

