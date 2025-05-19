from django.db import models

class Envio(models.Model):
    destinatario = models.CharField(max_length=100)
    documento = models.BigIntegerField()
    direccion = models.CharField(max_length=200)
    producto = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    objects = models.Manager()
    
    def __str__(self):
        return f"{self.destinatario} - {self.producto}"
