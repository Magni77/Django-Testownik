from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

departments = (
    ('w1', 'W1'),
    ('w2', 'W2'),
    ('w3', 'W3'),
    ('w4', 'W4 Elektroniki'),
)


class User(AbstractUser):
    department = models.CharField(choices=departments, max_length=2, blank=True)
    specialization = models.CharField(max_length=60, blank=True)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#
