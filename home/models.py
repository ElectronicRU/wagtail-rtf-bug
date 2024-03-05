from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin import panels


class HomePage(Page):
    content = RichTextField(blank=True, default='')

    content_panels = [
        panels.FieldPanel('content')
    ]
