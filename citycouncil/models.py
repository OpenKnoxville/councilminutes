# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Decision(models.Model):
    TYPES = (
        ('O', 'Ordinance'),
        ('R', 'Resoluation'),
    )

    code = models.CharField(max_length=16)
    decision_type = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField()
    text = models.TextField()
    discussion = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=256, blank=True, null=True)
    mover = models.CharField(max_length=256, blank=True, null=True)
    seconder = models.CharField(max_length=256, blank=True, null=True)
    ayes = models.CharField(max_length=1024, blank=True, null=True)
    nays = models.CharField(max_length=1024, blank=True, null=True)
    abstains = models.CharField(max_length=1024, blank=True, null=True)

    @property
    def short_text(self):
        return self.text[:150]
