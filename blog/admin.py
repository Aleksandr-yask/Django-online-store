from django.contrib import admin
from blog.models import *

# Register your models here.

class TagsPostInline(admin.TabularInline):
    model = TagsPost
    extra = 0

# ======================================================================================================

class PostImageInline(admin.TabularInline):
    model = PostImage

# ======================================================================================================


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    inlines = [
        TagsPostInline,
        PostImageInline,
    ]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

# ======================================================================================================

class PostImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostImage._meta.fields]

    class Meta:
        model = PostImage
        extra = 0

admin.site.register(PostImage, PostImageAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tags._meta.fields]

    class Meta:
        model = Tags
        extra = 0

admin.site.register(Tags, TagsAdmin)

# ======================================================================================================

# class TagsPostAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in TagsPost._meta.fields]
#
#     class Meta:
#         model = TagsPost
#         extra = 0
#
# admin.site.register(TagsPost, TagsPostAdmin)