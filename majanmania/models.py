from django.db import models

class Yaku(models.Model):
    CATEGORY =(('ippan','一翻'),
               ('ryanhan','二翻'),
               ('sanhan','三翻'),
               ('rohan','六翻'),
               ('yakuman','役満'),
               ('ryukyoku','流局')
               )
    category = models.CharField(
        verbose_name='役の種類',
        max_length=25,
        choices = CATEGORY

    )

    LOCAL = (('ippan','一般役'),
        ('rokaru','ローカル役')
            
            )
    
    local = models.CharField(
        verbose_name='ローカル役',
        max_length=25,
        choices = LOCAL
    )

    name = models.CharField(
        verbose_name='役の名前',
        max_length=50,
    )
    image = models.ImageField(
        verbose_name='イメージ',
        upload_to='photos'
    )

    setumeibun = models.TextField(
        verbose_name='説明'
    )

    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )
    def __str__ (self):
        return self.name