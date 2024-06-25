# Generated by Django 5.0.6 on 2024-06-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_alter_translation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('key', 'language')},
        ),
    ]
