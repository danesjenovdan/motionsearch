# Generated by Django 3.2 on 2021-05-10 19:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('motions', '0014_alter_motioncomment_created_at'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='motionvote',
            unique_together={('user', 'motion')},
        ),
    ]