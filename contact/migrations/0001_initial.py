# Generated by Django 3.1.6 on 2021-03-01 21:51

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='e-Mail')),
                ('subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='Assunto')),
                ('message', ckeditor.fields.RichTextField(max_length=1000, verbose_name='Mensagem')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
