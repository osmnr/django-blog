# Generated by Django 5.0.6 on 2024-06-25 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0004_translationkeys_alter_translation_key'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TranslationKeys',
            new_name='TranslationKey',
        ),
    ]