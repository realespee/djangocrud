from django.db import models

# Create your models here.
class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='record', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', )