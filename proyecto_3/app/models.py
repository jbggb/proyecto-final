from django.db import models
from datetime import datetime

# MODELOS QUE YA EXISTEN EN MAIN

class Administrador(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    usuario = models.CharField(max_length=50, unique=True, verbose_name="Usuario")
    contrasena = models.CharField(max_length=255, verbose_name="Contraseña")
    email = models.EmailField(max_length=100, verbose_name="Email")
    fechaRegistro = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "administrador"
        verbose_name_plural = "administradores"
        db_table = "administrador"


class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    fechaCasastro = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        db_table = "cliente"


class Marca(models.Model):
    nombreMarca = models.CharField(max_length=100, verbose_name="Nombre Marca")
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        db_table = "marca"


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    envio = models.IntegerField(default=1, verbose_name="Envío")
    fechaRegistro = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        db_table = "proveedor"


# TU NUEVO MODELO (PEDIDOS)

class Pedidos(models.Model):
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=150)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - {self.estado_pedido} - total: {self.total}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha_pedido']


class compra(models.Model):
    Administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_compra = models.DateField(default=datetime.now)
    totalcompra = models.FloatField()
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
