from django.db import models

# Create your models here.

class Text(models.Model):
    addtext = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.addtext