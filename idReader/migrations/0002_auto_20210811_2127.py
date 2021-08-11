# Generated by Django 3.1.5 on 2021-08-11 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idReader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitors',
            name='temp',
        ),
        migrations.RemoveField(
            model_name='visitors',
            name='visitee',
        ),
        migrations.AddField(
            model_name='visitors',
            name='addr_b4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='返阜前所在地'),
        ),
        migrations.AddField(
            model_name='visitors',
            name='desti_addr',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='目的地'),
        ),
        migrations.AddField(
            model_name='visitors',
            name='is_danger',
            field=models.BooleanField(blank=True, null=True, verbose_name='是否中高风险'),
        ),
        migrations.AddField(
            model_name='visitors',
            name='train_no',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='车次/航班'),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='户籍地址'),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='手机号'),
        ),
    ]