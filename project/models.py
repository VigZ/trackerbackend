from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

from account.models import User

from . import constants as c


class Tag(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)
    color = models.CharField(_('color'), max_length=256, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(_('display name'), max_length=30, blank=False)
    owner = models.ForeignKey(User, default=1, verbose_name="Owner", on_delete=models.SET_DEFAULT)
    admins = models.ManyToManyField(User, related_name="project_admins") # Through table for project admins
    members = models.ManyToManyField(User, related_name="project_members") # Through table for project members.

    def __str__(self):
        return self.project_name


class TicketGrouping(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)
    project = models.ForeignKey(Project, default=1, verbose_name="Project", on_delete=models.SET_DEFAULT)
    resolution_order = models.CharField(_('resolution_order'), max_length=1000, blank=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)
    poster = models.ForeignKey(User, default=1, verbose_name="Poster", on_delete=models.SET_DEFAULT)
    assigned_to = models.ManyToManyField(User, related_name="assignees")
    description = models.CharField(_('description'), max_length=1000, blank=True)
    environment = models.CharField(_('environment'), max_length=30, blank=True)
    attachment = models.FileField()
    tags = models.ManyToManyField(Tag, related_name="ticket_tags")
    due_date = models.DateTimeField(blank=True, null=True, help_text="The date before which the ticket is to be completed")
    completed_date = models.DateTimeField(blank=True, null=True, help_text="The date the ticket was completed")
    severity = models.CharField(_('severity'), choices=c.TICKET_SEVERITY_CHOICES, max_length=255, blank=False, default=c.TICKET_SEVERITY_CHOICES.normal)
    priority = models.CharField(_('priority'), choices=c.TICKET_PRIORITY_CHOICES, max_length=255, blank=False, default=c.TICKET_PRIORITY_CHOICES.mid)
    steps_to_reproduce = models.CharField(_('steps_to_reproduce'), max_length=1000, blank=True)
    ticket_grouping = models.ForeignKey(TicketGrouping, default=1, verbose_name="Ticket Grouping", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


class Comment(models.Model):
    poster = models.ForeignKey(User, default=1, verbose_name="Poster", on_delete=models.SET_DEFAULT)
    ticket = models.ForeignKey(Ticket, default=1, verbose_name="Ticket", on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    comment_text = models.CharField(_('comment_text'), max_length=1000, blank=False)
