# Generated by Django 4.0.4 on 2022-06-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sireproj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qtext', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='vesseldisc',
            name='Vtype',
            field=models.CharField(max_length=100),
        ),
    ]