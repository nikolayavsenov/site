# Generated by Django 3.0.3 on 2020-02-20 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Child_category', to='app.Cat', verbose_name='Parent_category')),
            ],
            options={
                'verbose_name': 'Cat',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tag')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Tagslug')),
            ],
            options={
                'verbose_name': 'TAG',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('mini_text', models.TextField(max_length=7)),
                ('text', models.TextField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=15, unique=True, verbose_name='POST')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Avtor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Cat', verbose_name='Categors')),
                ('tags', models.ManyToManyField(blank=True, to='app.Tag', verbose_name='Teg')),
            ],
            options={
                'verbose_name': 'POST',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('moderation', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post', verbose_name='Statii')),
            ],
        ),
    ]
