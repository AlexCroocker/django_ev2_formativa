from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    stock = models.PositiveSmallIntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido de {self.nombre} para {self.id_cliente.nombre}"
