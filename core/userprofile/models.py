from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    name = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_profile_detail', kwargs={'pk': self.pk})
