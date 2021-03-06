# Generated by Django 3.0.6 on 2020-07-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200730_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_text',
            field=models.TextField(max_length=130),
        ),
    ]
