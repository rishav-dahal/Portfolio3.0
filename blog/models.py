from django.db import models
from blog.utils import generate_unique_slug
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blogs/covers/',blank=True, null=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts_in_category')
    tags = models.ManyToManyField('Tag', blank=True,related_name='posts_with_tag')

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_published']),
        ]

    def save(self, *args, **kwargs):
    # Generate slug only for new instances when slug is empty
        if not self.slug and not self.pk:
            self.slug = self.generate_unique_slug()
        
        # For existing instances with empty slug (shouldn't happen), restore original slug
        elif not self.slug and self.pk:
            try:
                self.slug = BlogPost.objects.get(pk=self.pk).slug
            except BlogPost.DoesNotExist:
                self.slug = self.generate_unique_slug()
        
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'name')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'name')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

