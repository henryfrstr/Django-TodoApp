from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed  = models.BooleanField(default=False)
    cretaed = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ('completed', 'due')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("update_task", kwargs={"id": self.id})