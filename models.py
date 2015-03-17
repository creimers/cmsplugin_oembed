from django.db import models
from cms.models import CMSPlugin

# Create your models here.
from embed_video.fields import EmbedVideoField


class VideoPluginModel(CMSPlugin):
    name = models.CharField(
        blank=True,
        max_length=50
    )
    video_url = EmbedVideoField()

    def __unicode__(self):
        return u'%s' % self.name
