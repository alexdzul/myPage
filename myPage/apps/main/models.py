from django.db import models


class Setting(models.Model):

    def image_path(self, filename):
        ruta = "settings/%s/%s" % (self.settings_name, str(filename))
        return ruta


    settings_name = models.CharField(max_length=200)
    my_name = models.CharField(max_length=200)
    my_job = models.CharField(max_length=200)
    my_description = models.TextField(max_length=500)
    my_photo = models.ImageField(upload_to=image_path)
    background = models.ImageField(upload_to=image_path)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.settings_name

    class Meta:
        verbose_name = "Configuracion de la web"
        verbose_name_plural = "Configuraciones de la web"
