from django.db import models
from django.db.models.signals import post_save
from .utils import gen_code

class Project(models.Model):
    """ Stores a project created by me
        or a project I am currently
        contributing to
    """

    project_name = models.CharField(max_length=230)
    short_code = models.CharField(max_length=120, blank=True)
    project_description = models.TextField()
    project_url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_name}"

    class Meta:
        ordering = ['-created']


def post_save_receiver(instance, sender, *args, **kwargs):
    if not instance.short_code:
        instance.short_code = gen_code(size=8)
        instance.save()


post_save.connect(post_save_receiver, sender=Project)
