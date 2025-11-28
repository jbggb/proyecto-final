from django.db import models
from datetime import datetime
from decimal import Decimal

# ===============================
#        ADMINISTRADOR
# ===============================

class Administrador(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    usuario = models.CharField(max_length=50, unique=True, verbose_name="Usuario")
    contrasena = models.CharField(max_length=255, verbose_name="Contraseña")
    email = models.EmailField(max_length=100, verbose_name="Email")
    fechaRegistro = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "administrador"
        verbose_name_plural = "administradores"
        db_table = "administrador"


# ===============================
#            CLIENTE
# ===============================

class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    fechaCasastro = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        db_table = "cliente"


# ===============================
#             MARCA
# ===============================

class Marca(models.Model):
    nombreMarca = models.CharField(max_length=100, verbose_name="Nombre Marca")
    
    def __str__(self):
        return self.nombreMarca
    
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        db_table = "marca"


# ===============================
#       TIPO PRODUCTOS
# ===============================

class TipoProductos(models.Model):
    nombre_tipo = models.CharField(max_length=100, verbose_name="Nombre Tipo Producto")
    descripcion = models.TextField(verbose_name="Descripción Tipo Producto")

    def __str__(self):
        return self.nombre_tipo
    
    class Meta:
        verbose_name = "Tipo Producto"
        verbose_name_plural = "Tipos de Productos"
        db_table = "tipo_productos"


# ===============================
#      UNIDADES DE MEDIDA
# ===============================

class unidad_medida(models.Model):
    nombre_unidad = models.CharField(max_length=100, verbose_name="Nombre Unidad de Medida")
    abreviatura = models.CharField(max_length=10, verbose_name="Abreviatura")
    
    def __str__(self):
        return self.nombre_unidad
    
    class Meta:
        verbose_name = "unidad de medida"
        verbose_name_plural = "unidades de medida"
        db_table = "unidad_medida"


# ===============================
#      PRODUCTOS / INVENTARIO
# ===============================

class Producto(models.Model):
    idTipo = models.ForeignKey(TipoProductos, on_delete=models.CASCADE, db_column='idTipo')
    idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE, db_column='idMarca')
    idUnidad = models.ForeignKey(unidad_medida, on_delete=models.CASCADE, db_column='idUnidad')
    
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        db_table = "producto"


# ===============================
#               VENTAS
# ===============================

class Venta(models.Model):
    idAdministrador = models.IntegerField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='idCliente')
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='idProducto')
    
    fechaVenta = models.DateField(default=datetime.now, verbose_name="Fecha de Venta")
    totalVenta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Venta")
    
    def __str__(self):
        return f"Venta {self.id} - {self.fechaVenta}"
    
    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"
        db_table = "venta"


# ===============================
#            PROVEEDORES
# ===============================

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


# ===============================
#             PEDIDOS
# ===============================

class Pedidos(models.Model):
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=150)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - {self.estado_pedido}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        db_table = "pedidos"
        ordering = ['-fecha_pedido']


# ===============================
#              COMPRAS
# ===============================

class compra(models.Model):
    Administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    fecha_compra = models.DateField(default=datetime.now)
    totalcompra = models.FloatField()
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "compra"
