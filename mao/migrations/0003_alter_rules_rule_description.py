# Generated by Django 5.0.6 on 2024-05-21 06:04

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mao', '0002_rules_activation_rules_creator_rules_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rules',
            name='rule_description',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
