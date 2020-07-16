from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    long_url = models.URLField(null=True, blank=False)
    shortcode = models.CharField(blank=False,max_length=7)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.long_url

    def get_absolute_url(self):
        return reverse('redirect', kwargs={'slug':self.shortcode})