from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Group(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)


class UserManager(DjangoUserManager):

    def _create_user(self, email, password, is_staff,
                 is_superuser, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff,
                          is_active=True, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                             **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                             **extra_fields)


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
    groups = models.ManyToManyField(Group)
