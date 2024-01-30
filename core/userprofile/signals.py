from django.dispatch import receiver
from django.db.models.signals import post_save


from django.contrib.auth import get_user_model

from .models import UserProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(created, **kwargs):
    instance = kwargs['instance']
    print(instance)
    if created:
        new_profile = UserProfile(user_id=instance.pk)
        new_profile.save()
    else:
        print('Ни чего не делаю')