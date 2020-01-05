# Generated by Django 2.0 on 2020-01-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoSoft', '0002_auto_20200104_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.DateTimeField(max_length=30)),
            ],
        ),
    ]
