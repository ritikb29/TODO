from django.db import models

class Task (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title








    