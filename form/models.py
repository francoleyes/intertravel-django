from django.db import models

class Form(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="Nombre completo")
    email = models.CharField(max_length=70, verbose_name="Email")
    mobile = models.CharField(max_length=50, verbose_name="Número de teléfono")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"
        ordering = ['-created']

    def __str__(self):
        return self.full_name