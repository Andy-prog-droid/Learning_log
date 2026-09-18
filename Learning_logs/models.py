from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text


from django.db import models
# ... keep your Topic model as it is ...

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # ➕ 1. Add an edit counter field (starts at 0)
    edit_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."

    # ➕ 2. Override the save method to increase the count automatically on edits
    def save(self, *args, **kwargs):
        if self.id:  # If the entry already has an ID, it means it's being updated/edited
            self.edit_count += 1
        super().save(*args, **kwargs)
