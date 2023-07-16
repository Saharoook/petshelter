from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    image_content = models.ImageField(blank=True, upload_to='petshelter/images')
    image_content1 = models.ImageField(blank=True, upload_to='petshelter/images')
    image_content2 = models.ImageField(blank=True, upload_to='petshelter/images')
    created = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField()
    telegram_publication_flag = models.BooleanField(default=False)
    telegram_publication_flag_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Interactive(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    image_content = models.ImageField(blank=True, upload_to='petshelter/images')
    image_content1 = models.ImageField(blank=True, upload_to='petshelter/images')
    image_content2 = models.ImageField(blank=True, upload_to='petshelter/images')
    created = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField()
    telegram_publication_flag = models.BooleanField(default=False)
    telegram_publication_flag_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Pupil(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    image_content = models.ImageField(blank=True, upload_to='petshelter/images')
    image_content1 = models.ImageField(blank=True, upload_to='petshelter/images')
    image_content2 = models.ImageField(blank=True, upload_to='petshelter/images')
    age = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    kind = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField()
    telegram_publication_flag = models.BooleanField(default=False)
    telegram_publication_flag_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
