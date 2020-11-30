from django.db import models

# Create your models here.


class Contact(models.Model):

    user_email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user_email