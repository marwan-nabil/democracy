# Generated by Django 3.0.5 on 2020-04-30 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0004_auto_20200430_0217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='replymodel',
            options={'verbose_name': 'Reply', 'verbose_name_plural': 'Replies'},
        ),
        migrations.AddField(
            model_name='replymodel',
            name='with_thread',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
