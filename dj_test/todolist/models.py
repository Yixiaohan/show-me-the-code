from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Todolist(models.Model):
    user_name = models.CharField(max_length=255)
    todo = models.TextField()

    def __unicode__(self):
        return unicode(self.pk)

    class Meta:
        verbose_name = _(u'todolist')
