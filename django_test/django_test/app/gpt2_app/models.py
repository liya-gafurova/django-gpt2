from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return str(self.id)+'_'+str(self.title)
