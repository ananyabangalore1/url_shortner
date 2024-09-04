
from django.db import models
import string
import random

def generate_code():
    length = 6
    allowed_chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(allowed_chars) for i in range(length))

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=15, unique=True, default=generate_code)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs):
        while URL.objects.filter(short_code=self.short_code).exists():
            self.short_code = generate_code()
        super().save(*args, **kwargs)
