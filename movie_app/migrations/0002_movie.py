# Generated by Django 4.1.5 on 2023-01-14 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.FloatField(default=0)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director')),
            ],
        ),
    ]
