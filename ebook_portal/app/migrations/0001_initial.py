# Generated by Django 3.2.4 on 2021-06-08 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('publish_date', models.DateTimeField()),
                ('summary', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('cover_book_photo', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(max_length=12, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
