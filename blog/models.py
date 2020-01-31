from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pubdate.strftime('%b %e %Y')
