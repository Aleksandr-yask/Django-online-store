from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

# ======================================================================================================

class Post(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False, default=None)
    post = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

# ======================================================================================================

class TagsPost(models.Model):
    tag_name = models.ForeignKey(Tags, on_delete=models.CASCADE)
    tag_post = models.ForeignKey(Post, on_delete=models.CASCADE, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

# ======================================================================================================

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media/postImages/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'



