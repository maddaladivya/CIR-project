# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Announcements(models.Model):
    link = models.URLField(blank=True, null=True)
    expiry_date = models.DateField()

    @property
    def is_expired(self):
        if datetime.now > self.expiry_date:
            return True
        return False
