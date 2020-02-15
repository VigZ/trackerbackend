from django.db import models, IntegrityError
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

    # def save(self, *args, **kwargs):
    #     if self._owner_is_included():
    #         super(Project, self).save(*args, **kwargs)
    #     else:
    #         raise IntegrityError("Project owner must exist as an admin and member of the project.")


    def _owner_is_included(self):
        return self.admins.filter(id=self.owner.id).exists() and self.members.filter(id=self.owner.id).exists()


class TicketGrouping(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=False)
    project = models.ForeignKey(Project, default=1, verbose_name="Project", on_delete=models.SET_DEFAULT)
    resolution_order = models.CharField(_('resolution_order'), max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(_('name'), max_length=1000, blank=False)
    poster = models.ForeignKey(User, default=1, verbose_name="Poster", on_delete=models.SET_DEFAULT)
    assigned_to = models.ManyToManyField(User, related_name="assignees")
    description = models.CharField(_('description'), max_length=1000, blank=True)
    environment = models.CharField(_('environment'), max_length=30, blank=True)
    attachment = models.FileField()
    tags = models.ManyToManyField(Tag, related_name="ticket_tags")
    report_type = models.CharField(_('report_type'), choices=c.REPORT_TYPE_CHOICES, max_length=255, blank=True, default=c.REPORT_TYPE_CHOICES.other)
    due_date = models.DateTimeField(blank=True, null=True, help_text="The date before which the ticket is to be completed")
    completed_date = models.DateTimeField(blank=True, null=True, help_text="The date the ticket was completed")
    severity = models.CharField(_('severity'), choices=c.TICKET_SEVERITY_CHOICES, max_length=255, blank=False, default=c.TICKET_SEVERITY_CHOICES.normal)
    priority = models.CharField(_('priority'), choices=c.TICKET_PRIORITY_CHOICES, max_length=255, blank=False, default=c.TICKET_PRIORITY_CHOICES.mid)
    steps_to_reproduce = models.CharField(_('steps_to_reproduce'), max_length=1000, blank=True)
    ticket_grouping = models.ForeignKey(TicketGrouping, default=1, verbose_name="Ticket Grouping", on_delete=models.SET_DEFAULT)
    status = models.CharField(_('status'), choices=c.STATUS_CHOICES, max_length=255, blank=False, default=c.STATUS_CHOICES.pending)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def time_until_due_date(self):
            if self.due_date:
                return max(self.due_date - datetime.datetime.now, 0)
            return None

    def total_completion_time(self):
        if self.completed_date:
            return (self.completed_date - self.created_at)
        return "This ticket has not been completed yet."


class Comment(models.Model):
    poster = models.ForeignKey(User, default=1, verbose_name="Poster", on_delete=models.SET_DEFAULT)
    ticket = models.ForeignKey(Ticket, default=1, verbose_name="Ticket", on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_text = models.CharField(_('comment_text'), max_length=1000, blank=False)

    def __str__(self):
        return "Comment posted by " + self.poster.name
