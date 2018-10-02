from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="title here")
    subtitle = models.CharField(max_length=400, default="subtitle here")
    content = RichTextUploadingField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(default='', blank=True)
    thumbnail = models.ImageField(upload_to='blog/thumbnail')

    def publish(self):
        self.published_date = timezone.now()
        self.slug = slugify(self, title)
        self.save()

    def __str__(self):
        return self.title
