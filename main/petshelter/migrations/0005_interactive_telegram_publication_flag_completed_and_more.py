# Generated by Django 4.2.3 on 2023-07-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshelter', '0004_alter_news_image_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactive',
            name='telegram_publication_flag_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='telegram_publication_flag_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pupil',
            name='telegram_publication_flag_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='interactive',
            name='image_content',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='interactive',
            name='image_content1',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='interactive',
            name='image_content2',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_content1',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_content2',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='image_content',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='image_content1',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='image_content2',
            field=models.ImageField(blank=True, upload_to='petshelter/images'),
        ),
    ]
