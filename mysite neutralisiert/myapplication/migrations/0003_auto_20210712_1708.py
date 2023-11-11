# Generated by Django 3.2 on 2021-07-12 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0002_auto_20210706_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='dokument',
            field=models.FileField(default=datetime.datetime(2021, 7, 12, 17, 8, 28, 670064, tzinfo=utc), upload_to='application_documents/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationpapers',
            name='bezeichnung',
            field=models.CharField(choices=[('Arbeitszeugnis', 'Arbeitszeugnis'), ('Schulzeugnis', 'Schulzeugnis'), ('Bachelorzeugnis', 'Bachelorzeugnis'), ('Praktikumszeugnis', 'Praktikumszeugnis'), ('Urkunde', 'Urkunde'), ('IHK_Zeugnis', 'IHK_Zeugnis'), ('Lebenslauf', 'Lebenslauf'), ('Anschreiben', 'Anschreiben')], max_length=200),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='bezeichnung',
            field=models.CharField(choices=[('Code', 'Code'), ('Dokumentation', 'Dokumentation'), ('Bachelorarbeit', 'Bachelorarbeit')], max_length=200),
        ),
    ]