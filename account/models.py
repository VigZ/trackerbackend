from django.db import models
from django.contrib.auth.models import
from model_utils.models import TimeStampedModel


class User(TimeStampedModel, AbstractBaseUser):
    email = models.EmailField(
        _('email address'), unique=True,
        error_messages={
            'unique': _('A user with that email address already exists.'),
        })
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    display_name = models.CharField(_('display name'), max_length=30, blank=False)
    password = models.CharField(_('password'), max_length=100, blank=False)
