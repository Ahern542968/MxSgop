# Generated by Django 2.0 on 2018-10-14 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20181013_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default='', max_length=100, verbose_name='区域'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='province',
            field=models.CharField(default='', max_length=100, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='goods',
            field=models.ForeignKey(help_text='商品id', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
    ]