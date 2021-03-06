from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
        title = models.CharField(max_length=150)
        pub_date = models.DateTimeField()
        image = models.ImageField(upload_to='images/blog/')
        icon = models.ImageField(upload_to='images/blog/')
        body = models.TextField()
        url = models.TextField()
        votes_total = models.IntegerField(default=1)
        incubator = models.ForeignKey(User, on_delete=models.CASCADE)


        def __str__(self):
            return self.title

        def summary(self):
            return self.body[:200]



        def pub_date_pretty(self):
            return self.pub_date.strftime('%b %e %Y')
