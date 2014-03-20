 # -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Setting(models.Model):

    def image_path(self, filename):
        ruta = "settings/%s/%s"%(self.settings_name, str(filename))
        return ruta

    def my_photo_path(self, filename):
        ruta = "settings/%s/my_photo/%s"%(self.settings_name, str(filename))
        return ruta

    settings_name = models.CharField(max_length=100)
    my_name = models.CharField(max_length=100)
    my_job = models.CharField(max_length=100)
    my_description = models.TextField(max_length=500, null=True, blank=True)
    my_photo = models.ImageField(upload_to=my_photo_path)
    background = models.ImageField(upload_to=image_path)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.settings_name

    class Meta:
        verbose_name = "Configuración de la web"
        verbose_name_plural = "Configuraciones de la web"
