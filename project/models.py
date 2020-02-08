from django.db import models
from django.utils.translation import ugettext_lazy as _

from account.models import User


class Tag(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)


class Project(models.Model):
    project_name = models.CharField(_('display name'), max_length=30, blank=False)
    owner = models.ForeignKey(User, default=1, verbose_name="Owner", on_delete=models.SET_DEFAULT)
    admins = models.ManyToManyField(User, related_name="project_admins") # Through table for project admins

class Ticket(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)
    poster = models.ForeignKey(User, default=1, verbose_name="Poster", on_delete=models.SET_DEFAULT)
    assigned_to = models.ManyToManyField(User, related_name="assignees")
    description = models.CharField(_('description'), max_length=1000, blank=True)
    attachment = models.FileField()
    tags = models.ManyToManyField(Tag, related_name="ticket_tags")
