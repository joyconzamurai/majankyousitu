# Generated by Django 4.2.7 on 2023-11-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yaku',
            fields=[
                
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ippan', '一翻'), ('ryanhan', '二翻'), ('sanhan', '三翻'), ('rohan', '六翻'), ('yakuman', '役満'), ('ryukyoku', '流局')], max_length=25, verbose_name='役の種類')),
                ('local', models.CharField(choices=[('ippan', '一般役'), ('rokaru', 'ローカル役')], max_length=25, verbose_name='ローカル役')),
                ('name', models.CharField(max_length=50, verbose_name='役の名前')),
                ('image', models.ImageField(upload_to='photos', verbose_name='イメージ')),
                ('setumeibun', models.TextField(verbose_name='説明')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
            ],
        ),
    ]
