from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Feedback from {self.user.username} on {self.timestamp.strftime("%Y-%m-%d")}'
    
class Phone(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()

    tagline = models.CharField(max_length=200, blank=True, help_text="Short text for the homepage card")
    is_popular = models.BooleanField(default=False, help_text="Check this to show on Homepage")
    image = models.ImageField(upload_to='phones/', blank=True, null=True)

    ram = models.IntegerField()
    camera = models.IntegerField()
    battery = models.IntegerField()
    processor = models.CharField(max_length=50)
    display_type = models.CharField(max_length=50, db_column='displayType') # Match JS camelCase
    specs = models.JSONField()

    def __str__(self):
        return self.name
    
class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=50) 
    definition = models.TextField()
    example = models.TextField()

    class Meta:
        ordering = ['term']

    def __str__(self):
        return self.term