# Data model for blog Posts
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # Post title
    title = models.CharField(max_length= 250)
    # Used to build URLs for postes using their publish date and slug
    slug = models.SlugField(max_length= 250,
                            unique_for_date= 'publish')
    # Author of post
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name= 'blog_posts')
    # Body of the post
    body = models.TextField()
    # The datetime that the post was published
    publish = models.DateTimeField(default= timezone.now)
    # The datetime that the post was created
    created = models.DateTimeField(auto_now_add= True)
    # The datetime that the post was updated
    updated = models.DateTimeField(auto_now= True)
    # The status of the post (i.e. draft or published)
    status = models.CharField(max_length= 10,
                              choices= STATUS_CHOICES,
                              default='draft')
    # The default manager
    objects = models.Manager()
    # A custom manager
    published = PublishedManager()

    # Contains metadata for Post model
    class Meta:
        # Negative prefix sorts results in descending order so that recent posts
        # appear first
        ordering = ('-publish',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('blog:post_detail',
                          args=[self.publish.year,
                                self.publish.month,
                                self.publish.day,
                                self.slug])