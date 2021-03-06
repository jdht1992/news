# Generated by Django 2.1.2 on 2018-10-12 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500, null=True)),
                ('title', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=500, null=True)),
                ('url', models.URLField()),
                ('urltoimage', models.URLField()),
                ('publishedAt', models.DateField()),
                ('content', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Source'),
        ),
    ]
