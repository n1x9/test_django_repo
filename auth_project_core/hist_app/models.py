from django.db import models
from django.urls import reverse

# Create your models here.
class Hist(models.Model):
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=100)
    year = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk":self.id})

class Tag(models.Model):
    hist_tag = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.hist_tag)
#        return str(self.title)