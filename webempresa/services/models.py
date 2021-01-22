from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulum")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulum")
    content = models.TextField(verbose_name="Contenitum")
    image = models.ImageField(upload_to="services",  verbose_name="Imagenum")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacionum")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicionum")

    class Meta:
        verbose_name = "Serviciorum"
        verbose_name_plural = "Serviciorummis"
        ordering = ["-created"]  

    def __str__(self):
        return self.title 