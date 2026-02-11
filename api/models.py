from django.db import models

class Mensaje(models.Model):
    texto = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
