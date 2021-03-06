# Generated by Django 3.2.13 on 2022-05-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossessingBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('describe', models.CharField(max_length=500)),
                ('pubdate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WithBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200)),
                ('insertdate', models.CharField(max_length=200)),
                ('reqstatus', models.CharField(max_length=200)),
                ('statusmsg', models.CharField(max_length=200)),
                ('updatedate', models.CharField(max_length=200)),
            ],
        ),
    ]
