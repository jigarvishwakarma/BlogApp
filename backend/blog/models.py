from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
from django.template.defaultfilters import slugify

from django.conf import settings
UserAccount = settings.AUTH_USER_MODEL

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email


class Categories(models.TextChoices):
        WORLD = 'world'
        ENVIRONMENT = 'environment'
        TECHNOLOGY = 'technology'
        DESIGN = 'design'
        CULTURE = 'culture'
        BUSINESS = 'business'
        POLITICS = 'politics'
        OPINION = 'opinion'
        SCIENCE = 'science'
        HEALTH = 'health'
        STYLE = 'style'
        TRAVEL = 'travel'
        OTHERS = 'others'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = models.CharField(max_length=150, blank=False)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug
            
        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogBook(models.Model):
    blog = models.ManyToManyField(BlogPost)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = models.CharField(max_length=150, blank=False)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogBook.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogBook.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug
        super(BlogBook, self).save(*args, **kwargs)

    def __str__(self):
        return self.title