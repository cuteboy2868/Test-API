from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField(max_length=13)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Banner(models.Model):
    description = models.CharField(max_length=25)
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='product_photos/')
    category = models.ManyToManyField(Category)
    description = models.TextField()
    size_type = models.CharField(default='Kg', max_length=25)
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='client_photos/')
    job = models.CharField(max_length=25)
    comment = models.CharField(max_length=255)



class About_company(models.Model):
    video = models.CharField(max_length=255)
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog_photos/')
    date = models.DateField(auto_now=True)
    mini_text = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)



class Partner_brand(models.Model):
    img = models.ImageField(upload_to='brands/')



class Subscribe(models.Model):
    email = models.CharField(max_length=255)


class Service(models.Model):
    fast_name = models.CharField(max_length=25)
    fast_description = models.CharField(max_length=255)
    price_name = models.CharField(max_length=25)
    price_description = models.CharField(max_length=255)
    custom_name = models.CharField(max_length=25)
    custom_description = models.CharField(max_length=255)
    quick_name = models.CharField(max_length=25)
    quick_description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='service_photo/')


class Team(models.Model):
    photo = models.ImageField(upload_to='team_members_photos/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=25)
    instagram = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)


class Contact(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=255)
    message = models.TextField()


class Map(models.Model):
    lat = models.FloatField()
    lot = models.FloatField()


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    instagram = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)







