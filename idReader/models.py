from django.db import models


class Visitors(models.Model):
    visitor = models.CharField(max_length=6, null=True, blank=True, verbose_name='姓名')
    gender = models.BooleanField(null=True, blank=True, verbose_name='性别')
    id_no = models.CharField(max_length=18, null=True, blank=True, verbose_name='身份证号')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='户籍地址')
    phone = models.CharField(max_length=13, null=True, blank=True, verbose_name='手机号')
    addr_b4 = models.CharField(max_length=100, null=True, blank=True, verbose_name='返阜前所在地')
    desti_addr = models.CharField(max_length=100, null=True, blank=True, verbose_name='目的地')
    is_danger = models.BooleanField(null=True, blank=True, verbose_name='是否中高风险')
    train_no = models.CharField(max_length=100, null=True, blank=True, verbose_name='车次/航班')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='登记时间')
    valid = models.BooleanField(default=True, verbose_name='记录状态')
    bk1 = models.CharField(max_length=6, null=True, blank=True, verbose_name='bk1')
    bk2 = models.CharField(max_length=8, null=True, blank=True, verbose_name='bk2')
    bk3 = models.CharField(max_length=8, null=True, blank=True, verbose_name='bk3')

