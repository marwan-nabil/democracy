# Generated by Django 3.0.5 on 2020-04-30 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20200430_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadmodel',
            name='attached_image',
            field=models.ImageField(blank=True, null=True, upload_to='thread_images/%Y/%m/%d/'),
        ),
    ]
