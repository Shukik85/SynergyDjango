# Generated by Django 4.2.2 on 2023-06-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='профессия')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('surname', models.CharField(max_length=150, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=150, verbose_name='почта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('info', models.CharField(max_length=250, null=True, verbose_name='о себе')),
                ('photo', models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name='фото')),
                ('is_admin', models.BooleanField(default=False, verbose_name='администратор')),
                ('profession', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Shukik.profession', verbose_name='профессия')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ['-created_at'],
            },
        ),
    ]
