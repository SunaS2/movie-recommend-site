# Generated by Django 4.2.16 on 2024-11-25 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voca_notes', '0003_vocanotehistory'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vocanotehistory',
            unique_together=set(),
        ),
    ]
