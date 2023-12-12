from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Alumno(models.Model):
    usuario =models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null= True,
                                blank=True)
    nombre =models.CharField(max_length=200)
    apellido =models.CharField(max_length=200)
    completo =models.BooleanField(default=False)
    creado =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["completo"]
