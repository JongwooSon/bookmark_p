# Generated by Django 2.1 on 2019-04-30 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0005_auto_20190430_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='contents',
            new_name='content',
        ),
    ]